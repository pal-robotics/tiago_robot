^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Changelog for package tiago_controller_configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Forthcoming
-----------
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
* Contributors: Adolfo Rodriguez Tsouroukdissian, Bence Magyar, Jeremie Deray, Sam Pfeiffer, jordi.pages@pal-robotics.com

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
