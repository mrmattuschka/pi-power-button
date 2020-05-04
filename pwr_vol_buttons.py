#!/usr/bin/python3

import time
import subprocess
from gpiozero import Button, LED

##### Button actions #####

def vol_up():
    subprocess.run("amixer set Master 5%+", shell=True, check=True)

def vol_dn():
    subprocess.run("amixer set Master 5%-", shell=True, check=True)

def shutdown():
    subprocess.run("shutdown -h now", shell=True, check=True)

##### Set up buttons #####

button_vol_up   = Button(17, pull_up=True, hold_time=0.1)
button_vol_up.when_held = vol_up

button_vol_dn   = Button(27, pull_up=True, hold_time=0.1)
button_vol_dn.when_held = vol_dn

button_shutdown = Button(3, pull_up=True, hold_time=0.1)
button_shutdown.when_held = shutdown

while True:
    time.sleep(10)