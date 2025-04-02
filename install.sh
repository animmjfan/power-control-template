#!/bin/bash

#########################
##	   Setup Script    ##
#########################

# This script manually makes the required directories, folders and files for the script to run!
# by default this works under /usr/local/ and uses /usr/local/bin and /usr/local/lib and under /usr/local/lib it goes to /usr/local/lib/animmjfan/
# you can modify the name and path using variables and to get the default you keep status='default' if you want your changes to apply change it to status='custom'

program_name='Power control'
status='default'
if [[ $status == 'default' ]]; then
	echo "Are you sure you want to use default values for the installation?"
	echo "Default values will declare the installation path of the libaries to /usr/local/lib/ and the executable to /usr/local/bin/"
	echo "all under /usr/local/"
	echo "if you want to modify this then open this script in an editor, change the variables and make sure to change status to custom!"
	echo -n "are you sure you want to continue (press enter for yes and ctrl-c for no): "
	read
	echo "Okay then!"
	install_path='/usr/local/'
	libary_folder='/usr/local/lib/'
	binary_folder='/usr/local/bin/'
	author='animmjfan'
	co_author=''
elif [[ $status == 'custom' ]]; then
	# set/modify variables below
	# co_author is you and you can change the text that shows up with the authors to credit me after you or any way you want it to say it!!
	install_path='/usr/local/'
	libary_folder='/usr/local/lib/'
	binary_folder='/usr/local/bin/'
	author='animmjfan'
	co_author=''
	echo -e "install path is $(realpath $install_path)"
	echo -n "do you want to continue? press enter for yes: "
	read
	echo "Okay then!"
fi

newline () {
	echo
}

newline
newline
install_path=$(realpath $install_path)
libary_folder=$(realpath $libary_folder)
binary_folder=$(realpath $binary_folder)
echo 'starting install'
echo 'starting checks'
echo "checking the existance of the install path at '$install_path'"
if [ ! -d $install_path ]; then
	echo "$install_path doesn't exist yet, making it"
	mkdir $install_path
	echo "$install_path was made"
elif [ -d $install_path ]; then
	echo "$install_path already exists, skipping"
fi


echo "Welcome to $program_name!"