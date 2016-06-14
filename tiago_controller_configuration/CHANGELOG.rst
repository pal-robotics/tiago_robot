^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Changelog for package tiago_controller_configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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
