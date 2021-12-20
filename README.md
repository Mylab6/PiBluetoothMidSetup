# PiBluetoothMidSetup

## This will change serveral system wide packages/configurations 
## Do not run this on your primary machine or anything you don't know how to recover. 
Turn a Raspberry Pi into a Bluetooth Midi device , this assumes your using raspbian.
By default you still need to plug in a real usb midi device into the Raspberry PI, however it's very possible to send midi signals from software and transmit them via Bluetooh. While I may add this latter, it's not included with this release.  


Takes https://neuma.studio/rpi-midi-complete.html and wraps it into a nice automated script. 
I removed the OLED display step, so all you need to get started is a Rasbperry Pi( tested against a PI Zero with a otg cable). 
In the future I hope to get this working with Maschine controllers as well, but since they don't use a standard Midi connection that's a bit harder. 

### Old 
The Bluez installed here is a forked version to support Bluetooth Midi, forked again by me to fix a very minor C header issue. I've already submitted a PR, but until it's merged we'll have to use this : 
https://github.com/Mylab6/bluez
### Update, PR has been merged in , now using 
https://github.com/oxesoft/bluez

If you need to change your bluez version see 
https://github.com/Mylab6/PiBluetoothMidSetup/blob/b9e99cd215e1e6b85c8234ec7b80ac90d62a3005/setup_bt_commands.txt#L8
Tested against:
Rasberry Pi OS Lite(32 bit)
Released 2021-10-30.

### This can take anywhere from 20 to 30 minutes.

Run the following commands : 

sudo apt-get update


sudo apt-get install  git


Then run 

git clone https://github.com/Mylab6/PiBluetoothMidSetup

cd PiBluetoothMidSetup


sudo python3 setup_midi.py
