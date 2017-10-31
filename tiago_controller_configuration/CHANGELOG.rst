^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Changelog for package tiago_controller_configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Forthcoming
-----------

0.0.40 (2017-10-27)
-------------------

0.0.39 (2017-07-12)
-------------------

0.0.38 (2017-05-16)
-------------------

0.0.37 (2017-05-05)
-------------------

0.0.36 (2017-04-24)
-------------------
* Allow multiple Tiago to use the navigation stack
* Contributors: davidfernandez

0.0.35 (2016-12-21)
-------------------

0.0.34 (2016-11-06)
-------------------

0.0.33 (2016-11-04)
-------------------
* launch current_limit_controller of the gripper
* Contributors: Jordi Pages

0.0.32 (2016-10-26)
-------------------

0.0.31 (2016-10-14)
-------------------
* 0.0.30
* Update changelog
* Add missing dependencies
* modify package description
* add myself as maintainer
* add myself as maintainer
* 0.0.29
* Update changelog
* 0.0.28
* Update changelog
* 0.0.27
* Update changelog
* Removing shadow hand controllers
* 0.0.26
* Update changelog
* 0.0.25
* Update changelog
* 0.0.24
* changelog
* 0.0.23
* Update changelog
* 0.0.22
* Update changelog
* 0.0.21
* Update changelog
* Add imu_controller.launch
* 0.0.20
* Update changelog
* Remove wbc dependencies
* 0.0.19
* Update changelog
* Final values after testing in real robot
* Update gravity compensation parameters to new format
* 0.0.18
* changelog
* enable preserve_turning_radius
* enable wheel_data pub in mobile_base_controller
* 0.0.17
* changelog
* 0.0.16
* Update changelog
* Fix typo/copypaste on adding torso1 joint and 2 joint instead of gripper jointS
* 0.0.15
* Update changelog
* Add fake parallel gripper controller launch with only one joint
* 0.0.14
* Update changelog
* 0.0.13
* Update changelog
* Contributors: Jeremie Deray, Jordi Pages, Sam Pfeiffer, Victor Lopez


0.0.30 (2016-10-13)
-------------------
* Add missing dependencies
* modify package description
* add myself as maintainer
* add myself as maintainer
* Contributors: Jordi Pages, Victor Lopez

0.0.29 (2016-07-28)
-------------------

0.0.28 (2016-07-28)
-------------------

0.0.27 (2016-07-19)
-------------------
* Removing shadow hand controllers
* Contributors: Sam Pfeiffer

0.0.26 (2016-07-08)
-------------------

0.0.25 (2016-06-28)
-------------------

0.0.24 (2016-06-15)
-------------------

0.0.23 (2016-06-15)
-------------------

0.0.22 (2016-06-15)
-------------------

0.0.21 (2016-06-15)
-------------------
* Add imu_controller.launch
* Contributors: Victor Lopez

0.0.20 (2016-06-14)
-------------------
* Remove wbc dependencies
* Contributors: Victor Lopez

0.0.19 (2016-06-14)
-------------------
* Final values after testing in real robot
* Update gravity compensation parameters to new format
* Contributors: Sam Pfeiffer

0.0.18 (2016-06-14)
-------------------
* enable preserve_turning_radius
* enable wheel_data pub in mobile_base_controller
* Contributors: Jeremie Deray

0.0.17 (2016-06-13)
-------------------

0.0.16 (2016-06-13)
-------------------
* Fix typo/copypaste on adding torso1 joint and 2 joint instead of gripper jointS
* Contributors: Sam Pfeiffer

0.0.15 (2016-06-13)
-------------------
* Add fake parallel gripper controller launch with only one joint
* Contributors: Sam Pfeiffer

0.0.14 (2016-06-10)
-------------------

0.0.13 (2016-06-10)
-------------------

0.0.12 (2016-06-07)
-------------------
* Separating launch of joint_state_controller and force_torque_controller
* Contributors: Sam Pfeiffer

0.0.11 (2016-06-03)
-------------------
* Remove extra joints as the casters are not published anymore
* 0.0.10
* Updated changelog
* 0.0.9
* Update changelog
* 0.0.8
* Update changelog
* Add missing wbc dependencies to tiago_controller_configuration
  refs #13364
* 0.0.7
* Update changelog
* 0.0.6
* Update changelogs
* Fixed wheel sleeping in gazebo, and added head transmission (This can break the real robot if a blacklist is not implemented in pal_ros_control
* 0.0.5
* Update changelog
* Adding new defaults for TIAGo
  Current limit controller for the wheels.
  Soften on effort values config for a specific robot.
* launch Diff drive controller multipliers
* Removing specific current controller for wrist as the full arm one works already
* Compensate low force of joint 2
* tune parameters
* fix sign of arm 4
* Add gravity and wbc controllers load on boot
* remove hey5 hand from URDF
* Add extra_joints spec for joint state controller
  Only in hardware deployments: Load set of extra joints to be published as
  dummies by the joint_state_controller.
* Update finger pids so the hand works with PAL Hand plugin in gazebo
* Update with all joints until the grav compensation is fixed
  Add wrist controller
* Contributors: Adolfo Rodriguez Tsouroukdissian, Bence Magyar, Hilario Tome, Jeremie Deray, Sam Pfeiffer, Victor Lopez, jordi.pages@pal-robotics.com

0.0.4 (2015-05-20)
------------------
* Add current limit controller
* Fix name of spawner
* Add hand controller launch and config file
* Remove ref to hand
* Gravity compensation config & launch file
* Adding tiago_shadow, tiago with shadow lite hand (! no dependency on shadow packages on purpose!)
* Add install rule for home_gripper.py
* Contributors: Bence Magyar

0.0.3 (2015-04-15)
------------------

0.0.2 (2015-04-15)
------------------
* Move play_motion to controller launch files, update dependencies accordingly
* Add iron to startup
* Reduce acceleration limits
* add missing components for titanium+chessboard
* Add script to automatically open gripper
* Changes to fix finger shaking. Much better than before.
* Use steel and titanium tiago, launch files parametrized
* Change gripper joint names and add pids
* Change finger names and add controller + first gains
* Finetune of pids to prevent head shaking
* Add separate joint traj cont constraints for head
* Contributors: Bence Magyar, Enrique Fernandez, Jordi Pages

0.0.1 (2015-01-20)
------------------
* Load joint traj controllers config file
* Install config and launch files
* Add 0 pids for fingers
* Update inertias, Center of Mass' and related pids
  Hand commented until it works on gazebo
* Add tiago_bringup and tiago_controller_configuration
* Contributors: Bence Magyar
