# PiBluetoothMidSetup

## This will change serveral system wide packages/ configurations 
## Do not run this on your primary machine or anything you don't know how to recover. 
Turn a raspberry pi into a Bluetooth Midi device , this assumes your using raspbian


Takes https://neuma.studio/rpi-midi-complete.html and wrapps it into a nice automated script. 
I removed the OLED display step, so all you need to get started is a Rasbpery Pi( tested against a PI Zero with a otg cable). 
In the future I hope to get this working with Maschine controllers as well, but since they don't use a standard Midi connection that's a bit harder.  

Run the following commands : 

sudo apt-get update


sudo apt-get install  git


Then run 

git clone https://github.com/Mylab6/PiBluetoothMidSetup

cd PiBluetoothMidSetup


sudo python3 setup_midi.py
