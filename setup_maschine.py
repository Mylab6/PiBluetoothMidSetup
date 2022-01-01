import subprocess
import json 
import os 
import shutil

def set_up_maschine():
    subprocess.run("curl https://sh.rustup.rs -sSf | bash -s -- -y")
    subprocess.run("source $HOME/.cargo/env")
    results = subprocess.check_output("dmesg", universal_newlines=True).split('\n')
    for device in results:
        if "Native Instruments".lower() in device.lower():
            print(device)

    try:
        subprocess.run("git clone https://github.com/Mylab6/maschine.rs", shell=True, check=True)
    except:
        pass
    subprocess.run("cargo build --release", shell=True, check=True, cwd = get_local_file_path("maschine.rs") )
    subprocess.run("cargo run --release /dev/hidraw3", shell=True, check=True, cwd = get_local_file_path("maschine.rs") )

        

set_up_maschine()