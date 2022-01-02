# PiBluetoothMidSetup

## This will change serveral system wide packages/configurations 
## Do not run this on your primary machine or anything you don't know how to recover. 
Turn a Raspberry Pi into a Bluetooth Midi device , this assumes your using raspbian.
By default you still need to plug in a real usb midi device into the Raspberry PI, however it's very possible to send midi signals from software and transmit them via Bluetooh. While I may add this latter, it's not included with this release.  


Takes https://neuma.studio/rpi-midi-complete.html and wraps it into a nice automated script. 
I removed the OLED display step, so all you need to get started is a Rasbperry Pi( tested against a PI Zero with a otg cable). 

### Maschine instructions 


Install Rust 


curl https://sh.rustup.rs -sSf | bash -s -- -y
source $HOME/.cargo/env

Clone my fork of maschine.rs which contains a small fix(PR pending)


git clone https://github.com/Mylab6/maschine.rs

In maschine.rs folder 
cargo build --release

Finally, to run ( see run_maschine.py for an example, use dmesg to get the correct hidraw) 

sudo ./target/release/maschine /dev/" + find_hidraw(),




https://github.com/wrl/maschine.rs

Note, I've added a bit of functionality to automatically start the Maschine drivers, assuming you've done the above. 

If not the command silently fails, see run_maschine.py

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


### Notes: 

Appears to work with little to no latency. Will not work with a PI Zero/ Pi-Sugar, I suspect it simply isn’t getting enough power.  Tested on both PI Zero and PI Zero 2, this should work on any PI though. 

