#! /usr/bin/python3
from gpiozero import Button
import subprocess

button = Button(27)
button.wait_for_press()

subprocess.run(['sudo','/usr/sbin/shutdown', '-h', 'now'], shell=False)

