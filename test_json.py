import subprocess
import json 
import os 



files = json.loads( get_local_file_path("file_locations.json"))
for local_file in files: 
    print(local_file)
    #copy_file(local_file)
# run various commands 
#run_commands("setup_midi_commands.txt")
