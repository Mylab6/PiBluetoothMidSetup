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
        subprocess.run("sudo -u pi curl https://sh.rustup.rs -sSf | bash -s -- -y", shell=True)
        subprocess.run("sudo -u pi source $HOME/.cargo/env", shell=True)
    except:
        pass
    
    results = subprocess.check_output("sudo -u pi dmesg", universal_newlines=True, shell=True).split('\n')
    hdraw = ""
    for device in results:
        if "Native Instruments".lower() in device.lower() and "hidraw" in device.lower():
            print(device)
            hdraw = get_hdraw(device)

    try:
        subprocess.run("sudo -u pi git clone https://github.com/Mylab6/maschine.rs", shell=True, check=True)
    except:
        pass
    subprocess.run("sudo -u pi cargo build --release", shell=True, check=True, cwd = get_local_file_path("maschine.rs") )
    subprocess.run("sudo ./target/release/maschine  /dev/" + hdraw, shell=True, check=True, cwd = get_local_file_path("maschine.rs") )

        
if __name__ == "__main__":
    
    set_up_maschine()
