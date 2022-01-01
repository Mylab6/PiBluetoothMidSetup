import subprocess
import json 
import os 
import shutil

def set_up_maschine(self):
    results = subprocess.check_output("dmesg", shell=True, check=True,cwd = get_local_file_path(sub_dir))
    for device in results:
        if "Native Instruments" in device:
            print(device)

set_up_maschine()