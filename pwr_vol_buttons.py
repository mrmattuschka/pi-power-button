#!/usr/bin/python3

import time
import subprocess
import atexit
from gpiozero import Button, LED, DigitalOutputDevice, InputDevice

# Button actions

speaker = DigitalOutputDevice(22, active_high=True, initial_value=True)

def shutdown_speaker():
    speaker.off()
    speaker.close()
    speaker = InputDevice(22, pull_up=False)

def vol_up():
    subprocess.run("amixer -q set PCM 5%+", shell=True, check=True)

def vol_dn():
    subprocess.run("amixer -q set PCM 5%-", shell=True, check=True)

def shutdown():
    shutdown_speaker()
    subprocess.call(["shutdown", "-h", "now"], shell=False)
    

# Set up buttons

button_vol_up   = Button(17, pull_up=True, hold_time=0.1)
button_vol_up.when_held = vol_up

button_vol_dn   = Button(27, pull_up=True, hold_time=0.1)
button_vol_dn.when_held = vol_dn

button_shutdown = Button(3, pull_up=True, hold_time=0.1)
button_shutdown.when_held = shutdown

# Make sure to turn off speakers when this script exits

atexit.register(shutdown_speaker)

# Most importantly: keep doing nothing

while True:
    time.sleep(10)