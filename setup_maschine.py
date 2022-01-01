import subprocess
import json 
import os 
import shutil

import re

from setup_midi import get_local_file_path
def get_hdraw(regex):
    regexResult = re.search(",.*hidraw.*:",regex)
    return regexResult.group(0).replace(",","").replace(":","")

def set_up_maschine():
    try:
        subprocess.run("curl https://sh.rustup.rs -sSf | bash -s -- -y")
        subprocess.run("source $HOME/.cargo/env")
    except:
        pass
    
    results = subprocess.check_output("dmesg", universal_newlines=True).split('\n')
    hdraw = ""
    for device in results:
        if "Native Instruments".lower() in device.lower() and "hidraw" in device.lower():
            print(device)
            hdraw = get_hdraw(device)

    try:
        subprocess.run("git clone https://github.com/Mylab6/maschine.rs", shell=True, check=True)
    except:
        pass
    subprocess.run("cargo build --release", shell=True, check=True, cwd = get_local_file_path("maschine.rs") )
    subprocess.run("sudo ./target/release/maschine  /dev/" + hdraw, shell=True, check=True, cwd = get_local_file_path("maschine.rs") )

        
if __name__ == "__main__":
    
    set_up_maschine()
