^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Changelog for package tiago_controller_configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Forthcoming
-----------
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
