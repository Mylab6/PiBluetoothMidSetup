import subprocess
import json 
import os 

# first install bluez 
run_commands("setup_bt_commands.txt")
files = json.loads("file_locations.json")
for local_file in files: 
    copy_file(local_file)
# run various commands 
run_commands("setup_midi_commands.txt")

def run_commands(file_location):
    final_path = get_local_file_path( file_location)    
    file1 = open(final_path, 'r')
    Lines = file1.readlines()
    for command in Lines:
        subprocess.run(command, shell=True, check=True)
def copy_file(midi_file):    
    almost_file = os.path.join( 'files_to_copy' ,midi_file['repo_location'])
    file_to_cp = get_local_file_path(almost_file) 
    shutil.copy( file_to_cp, midi_file['file_sys_location'] )
    if( file_instance['make_exec']):
        exec('sudo chmod +x ' +  file_instance['file_sys_location'])
def get_local_file_path(sub_path):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    return os.path.join(dir_path,sub_path)