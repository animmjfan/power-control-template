#!/usr/bin/env python
#if anything goes wrong email me at animmjfan@gmail.com with your issuse and/or report it on github
#hope you like it...
#...and it works! pls!
throwawayvar = True
error = "An Error Occured"
def error():
    print(error)
    quit()
import os
if os.path.exists("/usr/local/lib/") == True:
    if os.path.exists("/usr/local/lib/animmjfan/usb-power-control/") == True:
        pass
    elif os.path.exists("/usr/local/lib/animmjfan/usb-power-control/") == False:
        os.mkdir("/usr/local/bin/animmjfan/usb-power-control/")
    else:
        error()
elif os.path.exists("/usr/local/lib/") == False:
    os.mkdir("/usr/local/lib/")
    os.mkdir("/usr/local/lib/animmjfan/usb-power-control/")
else:
    error()
import subprocess
while throwawayvar == True:
    with open("/usr/local/local/animmjfan/usb-power-control/on-off.txt", 'r') as file:
        content = file.read().strip()
    content
    if content == "1":
        subprocess.call('./usr/local/lib/animmjfan/usb-power-control/scripts/pwrON.sh')
    elif content == "0":
        subprocess.call('./usr/local/lib/animmfan/usb-power-control/scripts/pwrOFF.sh')
    elif content == "2":
        pass
    file.write("2")
