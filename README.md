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

##  Post Installation (After finishing step 6)
* Run `roscore` to make sure everything is installed correctly
* Move `sdformat.dll` from `C:\opt\rosdeps\x64\lib` to `C:\opt\rosdeps\x64\bin`
At this point the ROS and Gazebo environment should be all set. Try start gazebo `roslaunch gazebo_ros empty_world.launch`. This should bring up Gazebo up with an empty world.


## Robot Raconteur Gazebo Plugin
### Swig Installation
* Download Swig 4.0.2 [here](https://sourceforge.net/projects/swig/files/swigwin/swigwin-4.0.2/swigwin-4.0.2.zip/download?use_mirror=phoenixnap), and unzip it to `C:\` drive.
### Workspace Setup && RR Installation
* Create a folder named `catkin_ws` anywhere on your machine. Create a subfolder named `src` under that workspace.
* Inside `src\`, run following command:
```
git clone https://github.com/robotraconteur/robotraconteur.git
git clone –recurse https://github.com/johnwason/robotraconteur_standard_robdef_cpp.git 
git clone https://github.com/johnwason/RobotRaconteur_Gazebo_Server_Plugin.git
```
* Remove `gazebo_robotraconteur_server_plugin_examples\` folder under `\catkin_ws\src\RobotRaconteur_Gazebo_Server_Plugin/`.
* Go to `catkin_ws\`, build those packages using following command:
```
catkin_make_isolated -DROBOTRACONTEUR_ROS=1 -DSWIG_EXECUTABLE=C:\swigwin-4.0.2\swig.exe -DCMAKE_PROGRAM_PATH=C:\opt\rosdeps\x64\tools\protobuf -DCMAKE_BUILD_TYPE=Release
```
The building process may take half an hour or even longer.

## Run RR driver with Gazebo
* Clone this repo, and set environment variable `GAZEBO_MODEL_PATH` pointing to the `models` folder in this repo.
* The abstract robot service is provided in google drive.
* To start the robot service, run following command:
```
dotnet GazeboModelRobotRaconteurDriver.dll --gazebo-url=rr+tcp://localhost:11346/?service=GazeboServer --robotraconteur-tcp-port=58654 --robotraconteur-node-name=sawyer_robot  --model-name=sawyer --robot-info-file=sawyer_robot_default_config.yml
```
Adjust those parameters for different robots.

# Only run Gazebo related scripts in ROS cmd window

