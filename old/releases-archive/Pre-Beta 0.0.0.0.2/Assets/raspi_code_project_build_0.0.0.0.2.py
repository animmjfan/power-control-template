#this code is to be run off device in this case "device" is a raspi the raspi this project is made for is the raspi zero w 1.1 but any raspi zero w should work
#if anything goes wrong email me at anthonyfalzon12@icloud.com with your issuse and/or report it on github
#hope you like it...
#...and it works! pls!
throwawayvar = True
error = "An Error Occured"
def error():
    print(error)
    quit()
import os
if os.path.exists("/usr/local/bin/") == True:
    if os.path.exists("/usr/local/bin/raspi_project_by_animmjfan/") == True:
        pass
    elif os.path.exists("/usr/local/bin/raspi_project_by_animmjfan/") == False:
        os.mkdir("/usr/local/bin/raspi_project_by_animmjfan/")
    else:
        error()
elif os.path.exists("/usr/local/bin/") == False:
    os.mkdir("/usr/local/bin/")
    os.mkdir("/usr/local/bin/raspi_project_by_animmjfan/")
else:
    error()
import subprocess
while throwawayvar == True:
    with open("/usr/local/bin/raspi_project_by_animmjfan/importfrompi/on-off.txt", 'r') as file:
        content = file.read().strip()
    content
    if content == "1":
        subprocess.call('./usr/local/raspi_project_by_animmjfan/scripts/pwrON.sh')
    elif content == "0":
        subprocess.call('./usr/local/raspi_project_by_animmjfan/scripts/pwrOFF.sh')
    elif content == "2":
        pass
    file.write("2")
