# TIAGo robot

This package contains the description, controllers and bringup for all possible TIAGo configurations (end effectors, force torque sensors..).

To make maintenance easier, the `tiago.urdf.xacro` takes arguments that specify whether the robot has an arm or not, the end effector type, force torque sensor, laser model and many other parameters.

The other configuration files that differ between robot configurations are generated from template files.

The templates are written using [empy](https://pypi.org/project/empy/) and have the extension `.em`. 

To regenerate a group of files, you must execute `rosrun tiago_bringup regen_em_file.py EM_FILE_NAME` from the directory where the `.em` file is. 
