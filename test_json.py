import subprocess
import json 
import os 

def get_local_file_path(sub_path):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    return os.path.join(dir_path,sub_path)


files = json.load( open( get_local_file_path("file_locations.json")))
for local_file in files['files']: 
    print(local_file)
    #copy_file(local_file)
# run various commands 
#run_commands("setup_midi_commands.txt")
