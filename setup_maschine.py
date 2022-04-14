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
        subprocess.run("source $HOME/.cargo/env", shell=True)
    except:
        pass
    
  

    try:
        subprocess.run("git clone https://github.com/Mylab6/maschine.rs", shell=True, check=True)
    except:
        pass
    subprocess.run("$HOME/.cargo/bin/cargo build --release", shell=True, check=True, cwd = get_local_file_path("maschine.rs") )
    #old_file_location  = os.path.join( get_local_file_path("maschine.rs"),"maschine_files") 

      
if __name__ == "__main__":
    set_up_maschine()

