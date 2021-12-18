import subprocess
import json 

def copy_file(midi_file):
    file_to_cp = 'files_to_copy/' +  midi_file['repo_location'] 

    shutil.copy( file_to_cp, midi_file['file_sys_location'] )
    if( file_instance['make_exec']):
        exec('sudo chmod +x ' +  file_instance['file_sys_location'])


files = json.loads("file_locations.json")
for local_file in files: 
    copy_file(local_file)
# run various commands 

def set_up_midi_service():
  
def set_up_bluetooth():

def run_command(command):
    subprocess.run(command, shell=True, check=True)