# Installation
1. Clone the repo:

    git clone https://github.com/drewrl3v/virtualhome_alt.git

    cd virtualhome_alt

1. Create your virtual environment:

    python3 -m venv vhome

    source vhome/bin/activate

2. pip install virtualhome

    python3 -m pip install -e .

# Running an X server

1. sudo python3 virtualhome/helper_scripts/startx.py 1
2. python3 examples/test.py
    

# Killing A Rogue Procees

1. If your linux binary keeps persisting and spawning:

    ps aux | grep linux_exec.v2.2.4.x86_64

    kill -9 PID

    