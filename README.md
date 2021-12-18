# PiBluetoothMidSetup
Turn a raspberry pi into a Bluetooth Midi device 


Takes https://neuma.studio/rpi-midi-complete.html and wrapps it into a nice automated script. 

Everything is taken care of, except for 
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install ruby git

Then run 
git clone https://github.com/Mylab6/PiBluetoothMidSetup
cd PiBluetoothMidSetup
sudo python3 setup_midi.py