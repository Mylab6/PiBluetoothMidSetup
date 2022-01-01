import subprocess
import json 
import os 
import shutil

def run_commands(file_location, sub_dir = None):
    final_path = get_local_file_path( file_location)    
    file1 = open(final_path, 'r')
    Lines = file1.readlines()
    for command in Lines:
        if(sub_dir):
            subprocess.run(command, shell=True, check=True,cwd = get_local_file_path(sub_dir))

        else: 
            subprocess.run(command, shell=True, check=True)
def copy_file(midi_file):    
    almost_file = os.path.join( 'files_to_copy' ,midi_file['repo_location'])
    file_to_cp = get_local_file_path(almost_file) 
    shutil.copy( file_to_cp, midi_file['file_sys_location'] )

def get_local_file_path(sub_path):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    return os.path.join(dir_path,sub_path)


if __name__ == "__main__":  
# Then copy the files 
    files = json.load( open( get_local_file_path("file_locations.json")))
#for local_file in files['files']: 
    for local_file in files['files']: 
        copy_file(local_file)
# run various commands 

# first install bluez 
  
    run_commands("setup_bt_commands.txt")
    run_commands("setup_bluez.txt","bluez")
# Feel free to comment anything out if the install gets stuck after like the first 2 commands. 
# Setting up bluez takes a minute, make some tea or something .
    run_commands("setup_midi_commands.txt")
    print("Bluetooth midi setup done") 
