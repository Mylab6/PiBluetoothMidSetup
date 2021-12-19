# PiBluetoothMidSetup

## This will change serveral system wide packages/ configurations 
## Do not run this on your primary machine or anything you don't know how to recover. 
Turn a raspberry pi into a Bluetooth Midi device , this assumes your using raspbian


Takes https://neuma.studio/rpi-midi-complete.html and wrapps it into a nice automated script. 

Everything is taken care of, except for

sudo apt-get update


sudo apt-get install  git


Then run 
git clone https://github.com/Mylab6/PiBluetoothMidSetup
cd PiBluetoothMidSetup
sudo python3 setup_midi.py
