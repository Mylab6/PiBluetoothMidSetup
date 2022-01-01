import subprocess
import json 
import os 
import shutil

def set_up_maschine():
    results = subprocess.check_output("dmesg", shell=True, check=True)
    for device in results:
        if "Native Instruments" in device:
            print(device)

set_up_maschine()