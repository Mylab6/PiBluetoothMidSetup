import subprocess


import re

from setup_midi import get_local_file_path

binary_location = "./target/release/maschine"
def get_hdraw(regex):
    regexResult = re.search(",.*hidraw.*:",regex)
    return regexResult.group(0).replace(",","").replace(":","")     
def find_hidraw():
    results = subprocess.check_output("sudo -u pi dmesg", universal_newlines=True, shell=True).split('\n')
    hdraw = ""
    for device in results:
        if "Native Instruments".lower() in device.lower() and "hidraw" in device.lower():
            print(device)
            hdraw = get_hdraw(device)
    print("Using HID", hdraw )
    return hdraw

def run_maschine():
    subprocess.run("sudo " + binary_location + " /dev/" + find_hidraw(), shell=True, check=True, cwd = get_local_file_path("maschine.rs") )

  

if __name__ == "__main__":
        run_maschine()


