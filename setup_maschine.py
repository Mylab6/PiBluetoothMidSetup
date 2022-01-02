import subprocess
import json 
import os 
import shutil
from os.path import exists


import re

from setup_midi import get_local_file_path
binary_location = "./target/release/maschine"


def set_up_maschine():
    try:
        subprocess.run("curl https://sh.rustup.rs -sSf | bash -s -- -y", shell=True)
        subprocess.run("pi source $HOME/.cargo/env", shell=True)
    except:
        pass
    
  

    try:
        subprocess.run("git clone https://github.com/Mylab6/maschine.rs", shell=True, check=True)
    except:
        pass
    subprocess.run("cargo build --release", shell=True, check=True, cwd = get_local_file_path("maschine.rs") )

      
if __name__ == "__main__":
    set_up_maschine()

