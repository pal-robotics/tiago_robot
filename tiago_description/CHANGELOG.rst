^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Changelog for package tiago_description
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Forthcoming
-----------
* Remove gazebo dependency
* Increase speed of torso joint
* Add tiago iron urdf
* Refactor gripper to ${name}
* Added grasping frame
* rotate chessboard and use degrees in its RPY
* Stop fingers shaking and add grasping hack
* add missing components for titanium+chessboard
* rename frame
* Tweak inertial params
* better placement of chessboard
* Add URDF with chessboard attached to hand
  For eye-hand calibration in simulation
* Changes to fix finger shaking. Much better than before.
* Use steel and titanium tiago, launch files parametrized
* Change gripper joint names and add pids
* Change finger names and add controller + first gains
* Add tiago_steel and tiago_gripper sketch
* Parametrize on robot type (tiago_X)
* Activate hand
* Make DarkGrey darker
* Change occureces of ant_ to pmb2_
* Update xtion with inertias and adding _link to parent inside
* Add nice visual to head2
* Update torso with reviewed inertial params
* Contributors: Bence Magyar, Jordi Pages

0.0.1 (2015-01-20)
------------------
* Fix orientation of head joint
* Comment actuator specification in transmission so that pal_ros_control won't take control of them.
* Comment joint mode related parts
* Add transmission to torso
* Add _use_gui:=True
* Remove config from install rule
* Don't append _link to parent value
* Update joint limits of head, 45degs up, 90degs down
* Remove unused sensors and fix link to mesh in xtion
* Update inertias, Center of Mass' and related pids
  Hand commented until it works on gazebo
* Add tiago hardware to description
* add arg
* Update distances
* Fix arm location
* Add head based on v2 drawing
* Add joint limits and rotate wrist according to v3
* arm v2, extensions of the same length
* Fix optical frame alignment
* Add preliminary head
* Update joint limits
* Fix torso
* Add visual & collision before wrist
* Fix visuals on arm
* Add hey5 hand to tiago
* Remove duplicated ant stuff and pull mobile base from ant_description
* Add arm and adjust torso
* Updated torso
* Initial commit
* Contributors: Bence Magyar, Hilario Tome
