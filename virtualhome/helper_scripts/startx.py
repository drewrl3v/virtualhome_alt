import subprocess
import shlex
import re
import platform
import tempfile
import os
import sys

def pci_records():
    records = []
    command = shlex.split('lspci -vmm')
    output = subprocess.check_output(command).decode()

    for devices in output.strip().split("\n\n"):
        record = {}
        records.append(record)
        for row in devices.split("\n"):
            key, value = row.split("\t")
            record[key.split(':')[0]] = value

    return records

def generate_xorg_conf(devices):
    xorg_conf = []

    device_section = """
Section "Device"
    Identifier     "Device{device_id}"
    Driver         "nvidia"
    VendorName     "NVIDIA Corporation"
    BusID          "{bus_id}"
EndSection
"""
    server_layout_section = """
Section "ServerLayout"
    Identifier     "Layout0"
    {screen_records}
EndSection
"""
    screen_section = """
Section "Screen"
    Identifier     "Screen{screen_id}"
    Device         "Device{device_id}"
    DefaultDepth    24
    Option         "AllowEmptyInitialConfiguration" "True"
    SubSection     "Display"
        Depth       24
        Virtual 1024 768
    EndSubSection
EndSection
"""
    screen_records = []
    for i, bus_id in enumerate(devices):
        xorg_conf.append(device_section.format(device_id=i, bus_id=bus_id))
        xorg_conf.append(screen_section.format(device_id=i, screen_id=i))
        screen_records.append('Screen {screen_id} "Screen{screen_id}" 0 0'.format(screen_id=i))

    xorg_conf.append(server_layout_section.format(screen_records="\n    ".join(screen_records)))

    output =  "\n".join(xorg_conf)
    print(output)
    return output

def stopx(display):
    """Stop X server on the specified display."""
    try:
        # Find the PID of the Xorg process running on the specified display
        output = subprocess.check_output(['ps', 'aux']).decode()
        for line in output.splitlines():
            if f"Xorg :{display}" in line:
                pid = int(line.split()[1])
                print(f"Stopping X server on display :{display} (PID {pid})")
                subprocess.call(['kill', '-9', str(pid)])
                break
    except Exception as e:
        print(f"Failed to stop X server on display :{display}: {e}")

def startx(display, gpu_id):
    if platform.system() != 'Linux':
        raise Exception("Can only run startx on linux")

    # Stop the X server if it's already running on this display
    stopx(display)

    devices = []
    records = pci_records()
    for r in records:
        if r.get('Vendor', '') == 'NVIDIA Corporation' \
                and r['Class'] in ['VGA compatible controller', '3D controller']:
            bus_id = 'PCI:' + ':'.join(map(lambda x: str(int(x, 16)), re.split(r'[:\.]', r['Slot'])))
            devices.append(bus_id)

    if not devices:
        raise Exception("no nvidia cards found")
    
    if len(gpu_id) > 0:
        devices = [devices[gpid] for gpid in gpu_id]
    
    try:
        with tempfile.NamedTemporaryFile(delete=False) as f:
            xorg_conf_path = f.name
            f.write(generate_xorg_conf(devices).encode('utf-8'))
        
        command = shlex.split(f"Xorg -noreset +extension GLX +extension RANDR +extension RENDER -config {xorg_conf_path} :{display}")
        result = subprocess.call(command)
        if result != 0:
            raise RuntimeError(f"Xorg command failed with return code {result}")
    finally:
        os.unlink(xorg_conf_path)

if __name__ == '__main__':
    display = 1  # Change to the display you want to manage
    gpu_id = []
    if len(sys.argv) > 1:
        display = int(sys.argv[1])
        if len(sys.argv) > 2:
            gpu_id = [int(x) for x in sys.argv[2].split(',')]
    
    print(f"Restarting X on DISPLAY=:{display} with gpu {gpu_id}")
    startx(display, gpu_id)
