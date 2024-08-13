from virtualhome.simulation.unity_simulator import comm_unity, UnityCommunication
#YOUR_FILE_NAME = "Your path to the simulator" # e.g.  ./linux_exec.v2.2.4.x86_64
YOUR_FILE_NAME = "/home/alizarra/repos/multi-agent-lora-llm/vhome_examples/linux_exec.v2.2.4.x86_64" # e.g.  ./linux_exec.v2.2.4.x86_64
#comm = UnityCommunication(file_name=YOUR_FILE_NAME, port="8080", x_display="1")
comm = UnityCommunication(file_name=YOUR_FILE_NAME, x_display="1")

# Start the first environment
comm.reset(0)
# Get an image of the first camera
success, image = comm.camera_image([0])

# Check that the image exists
print(image[0].shape)