#!/usr/bin/env python

# if anything goes wrong email me at animmjfan@gmail.com with your issuse and/or report it on github
# hope you like it...
# ...and hope it works! pls!

import subprocess

while True:
    with open("/usr/local/lib/power-control/on-off.txt", 'r') as file:
        content = file.read().strip()
    content
    if content == "1":
        subprocess.call('./usr/local/lib/power-control/scripts/pwrON.sh')
    elif content == "0":
        subprocess.call('./usr/local/lib/power-control/scripts/pwrOFF.sh')
    elif content == "2":
        pass
    file.write("2")
