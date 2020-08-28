# Instructions for Installing ROS Noetic on Win10 (come with Gazebo9)

Follow installation guide on http://wiki.ros.org/Installation/Windows. At step 5, choose Noetic, and just install ROS1.

## Important
* The Windows version is crude, the installation will take hours
* All command prompt windows should be opened with administrator
* Disable firewall
* Uninstall Python3.7 (If you have it)
* Name all other possible python.exe to its version (if you have other versions, such as python.exe in python38, name it to python38.exe)


## Notes on Step 5
There might be errors while installing. The process will install python3.7 for you, if there're errors with python, try
* Make sure `python` command will bring up python3.7 under `C:\opt\python37amd64`
* Add `C:\opt\ptyhon37` to your [Environment Variable](https://www.architectryan.com/2018/08/31/how-to-change-environment-variables-on-windows-10/)
* Install numpy 1.18.0, `python -m pip install numpy==1.18.0`
* Install empy, `python -m pip install empy`

##  Post Installation
