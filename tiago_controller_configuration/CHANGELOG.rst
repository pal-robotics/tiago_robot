^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Changelog for package tiago_controller_configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

2.3.7 (2022-08-10)
------------------
* Merge branch 'fix_torso_collision' into 'erbium-devel'
  Fix collision boxes for the torso
  See merge request robots/tiago_robot!156
* Reorder param order for making it easier to spot
* Remove extra joints because were changed to fixed
* Contributors: saikishor, thomaspeyrucain

2.3.6 (2022-08-04)
------------------

2.3.5 (2022-07-26)
------------------
* Merge branch 'omnibase_wbc' into 'erbium-devel'
  propagate base_type to wbc
  See merge request robots/tiago_robot!155
* propagate base_type to wbc
* Contributors: saikishor, thomaspeyrucain

2.3.4 (2022-07-21)
------------------
* Merge branch 'add_omni_tiago' into 'erbium-devel'
  Add base_type to the missing launch files
  See merge request robots/tiago_robot!153
* =Add base_type to the missing launch files
* Contributors: saikishor, thomaspeyrucain

2.3.3 (2022-07-19)
------------------
* Removed extra space in the filename
* Contributors: antoniobrandi

2.3.2 (2022-05-17)
------------------

2.3.1 (2022-05-16)
------------------

2.3.0 (2022-05-03)
------------------

2.2.15 (2022-05-03)
-------------------
* Merge branch 'no-end-effector-bugfix' into 'erbium-devel'
  No end effector bugfix
  See merge request robots/tiago_robot!149
* remove redundant spaces
* remove redundant spaces
* Added no end-effector to cartesian impedance controller.launch
* made some changes
* Update eval function, generate scripts
* rebase
* rebase
* Added no end-effector to cartesian impedance controller.launch
* made some changes
* Update eval function, generate scripts
* rebaed
* Added no end-effector to cartesian impedance controller.launch
* made some changes
* Update eval function, generate scripts
* Added no end-effector to cartesian impedance controller.launch
* made some changes
* Update eval function, generate scripts
* Contributors: David ter Kuile, saikishor

2.2.14 (2022-04-20)
-------------------

2.2.13 (2022-03-23)
-------------------
* Merge branch 'fix_home_robotiq_2f_140' into 'erbium-devel'
  Fix home position for robotiq-2f-140 + fix Reach max out of range motion + add effort_controller
  See merge request robots/tiago_robot!148
* Fix home position for robotiq-2f-140 + fix Reach max out of range motion + add effort_controller
* Contributors: saikishor, thomaspeyrucain

2.2.12 (2022-03-18)
-------------------

2.2.11 (2022-03-18)
-------------------
* Merge branch 'add_robotiq_epick_gripper' into 'erbium-devel'
  Add link to epick urdf
  See merge request robots/tiago_robot!145
* Change config files to match new name and new controller + add joystick control
* Change the name from vacuum to finger and add config file for controller
* Add config files for robotiq-epick gripper
* Contributors: saikishor, thomaspeyrucain

2.2.10 (2022-02-22)
-------------------

2.2.9 (2022-01-19)
------------------

2.2.8 (2021-12-22)
------------------
* Merge branch 'reduced_wbc' into 'erbium-devel'
  Add argument to set torso to no control
  See merge request robots/tiago_robot!144
* Add argument to set torso to no control
* Contributors: Adria Roig, narcismiguel

2.2.7 (2021-11-25)
------------------

2.2.6 (2021-11-22)
------------------
* Merge branch 'fix-omnibase' into 'erbium-devel'
  Configuration of the speed filters for the combined mouvements of the omni base
  See merge request robots/tiago_robot!142
* Configuration of the speed filters for the combined mouvements of the omni base
* Contributors: antoniobrandi, saikishor

2.2.5 (2021-11-19)
------------------
* Merge branch 'conditional_dependencies' into 'erbium-devel'
  Conditional dependencies
  See merge request robots/tiago_robot!140
* added PAL_DISTRO conditioning for PAL dependencies
* change to package version 3
* Contributors: Sai Kishor Kothakota, victor

2.2.4 (2021-11-10)
------------------
* added cartesian_impedance_controller controller as dependency
* Contributors: Sai Kishor Kothakota

2.2.3 (2021-11-10)
------------------
* Merge branch 'omni_base_fix' into 'erbium-devel'
  Reducing speed limit in order to avoid a wheel blocking
  See merge request robots/tiago_robot!139
* Reducing speed limit in order to avoid a wheel blocking
* Contributors: antoniobrandi, saikishor

2.2.2 (2021-11-09)
------------------
* Merge branch 'cartesian_impedance' into 'erbium-devel'
  Added the cartesian impedance config and launch file
  See merge request robots/tiago_robot!132
* added the gains for the controller
* Added the cartesian impedance config and launch file
* Contributors: Sai Kishor Kothakota, saikishor

2.2.1 (2021-11-09)
------------------

2.2.0 (2021-11-03)
------------------
* Merge branch 'omni_base_robot' into 'erbium-devel'
  Omni base robot
  See merge request robots/tiago_robot!137
* added dynamic footprint configuration for tiago with omni_base
* preparing configuration for a tiago with omni base
* Contributors: antoniobrandi, saikishor

2.1.5 (2021-09-22)
------------------

2.1.4 (2021-08-31)
------------------
* Merge branch 'kangaroo_wbc' into 'erbium-devel'
  Kangaroo wbc
  See merge request robots/tiago_robot!134
* Add BS parameters needed for local joint control
* Contributors: Adria Roig, victor

2.1.3 (2021-08-06)
------------------
* Merge branch 'robotiq-impedance-issues' into 'erbium-devel'
  fix: missing chain definition for robotiq gripper
  See merge request robots/tiago_robot!131
* refact: unify condition
* fix: missing chain definition for robotiq gripper
* Contributors: daniellopez, saikishor

2.1.2 (2021-07-16)
------------------

2.1.1 (2021-06-01)
------------------
* Merge branch 'impedance_controllers' into 'erbium-devel'
  added impedance controller configuration
  See merge request robots/tiago_robot!126
* Fix the actuator name in arm_1_joint
* fix: endless loop in joint 6
* added impedance controller configuration
* Contributors: Sai Kishor Kothakota, daniellopez, saikishor, victor

2.1.0 (2021-05-06)
------------------
* Merge branch 'robotiq_gripper' into 'erbium-devel'
  Robotiq gripper
  See merge request robots/tiago_robot!125
* add robotiq dependencies and robotiq grippers to the tests
* added the gravity compensation configurations for robotiq grippers
* Update the joint trajectory controller config yamls
* Contributors: Sai Kishor Kothakota, saikishor

2.0.58 (2021-04-09)
-------------------

2.0.57 (2021-03-19)
-------------------

2.0.56 (2021-03-01)
-------------------

2.0.55 (2021-01-15)
-------------------
* Merge branch 'gravity_compensation_fix' into 'erbium-devel'
  Update arm_3_link weight for gravity compensation
  See merge request robots/tiago_robot!120
* Update motor torque constant arm_5_joint for gravity_compensation
* Contributors: Adria Roig, victor

2.0.54 (2020-09-08)
-------------------
* Merge branch 'new-endoscopic-dual' of gitlab:robots/tiago_robot into new-endoscopic-dual
* Contributors: daniellopez

2.0.53 (2020-07-30)
-------------------

2.0.52 (2020-07-27)
-------------------
* Merge branch 'safety_parameters' into 'erbium-devel'
  Update default_safety_parameters.yaml with new changes in the safety of local joint control
  See merge request robots/tiago_robot!117
* Update default_safety_parameters.yaml with new changes in the safety of local joint control
* Contributors: saikishor, victor

2.0.51 (2020-07-15)
-------------------

2.0.50 (2020-07-10)
-------------------

2.0.49 (2020-07-01)
-------------------

2.0.48 (2020-06-10)
-------------------

2.0.47 (2020-05-15)
-------------------

2.0.46 (2020-05-13)
-------------------

2.0.45 (2020-05-12)
-------------------

2.0.44 (2020-05-12)
-------------------

2.0.43 (2020-05-08)
-------------------

2.0.42 (2020-05-07)
-------------------

2.0.41 (2020-05-07)
-------------------

2.0.40 (2020-05-06)
-------------------

2.0.39 (2020-04-21)
-------------------
* Merge branch 'custom-ee' into 'erbium-devel'
  Allow using custom end-effector
  See merge request robots/tiago_robot!102
* Add parameter files for custom EE
* Contributors: davidfernandez, victor

2.0.38 (2020-02-27)
-------------------

2.0.37 (2020-02-14)
-------------------

2.0.36 (2020-01-28)
-------------------
* Merge branch 'specifics_file' into 'erbium-devel'
  added missing actuator specifics file
  See merge request robots/tiago_robot!100
* added missing actuator specifics file
* Contributors: Sai Kishor Kothakota, Victor Lopez

2.0.35 (2019-11-06)
-------------------

2.0.34 (2019-10-30)
-------------------

2.0.33 (2019-10-21)
-------------------

2.0.32 (2019-10-16)
-------------------

2.0.31 (2019-10-10)
-------------------

2.0.30 (2019-10-02)
-------------------

2.0.29 (2019-09-27)
-------------------

2.0.28 (2019-09-25)
-------------------

2.0.27 (2019-09-17)
-------------------
* added missing effort control parameters for arm joint 4
* Contributors: Hilario Tome

2.0.26 (2019-07-18)
-------------------

2.0.25 (2019-07-09)
-------------------
* Merge branch 'add-wsg-controller-dependency' into 'erbium-devel'
  Add missing wsg controller config
  See merge request robots/tiago_robot!89
* Add missing wsg controller config
* Contributors: Victor Lopez

2.0.24 (2019-07-08)
-------------------

2.0.23 (2019-06-07)
-------------------
* Merge branch 'joint_traj_bug' into 'erbium-devel'
  Fixes bjoin trajectory bug in torso controller
  See merge request robots/tiago_robot!87
* Fixes bjoin trajectory bug in torso controller
* Contributors: Adria Roig, Victor Lopez

2.0.22 (2019-05-21)
-------------------

2.0.21 (2019-05-13)
-------------------

2.0.20 (2019-05-09)
-------------------
* Merge branch 'no_wrist_gravity' into 'erbium-devel'
  Add gravity no wrist for new wrist model
  See merge request robots/tiago_robot!81
* Update motor_torque_constant for the joints of the wrist
* Add gravity no wrist for new wrist model
* Contributors: Adria Roig, Victor Lopez

2.0.19 (2019-05-02)
-------------------

2.0.18 (2019-04-23)
-------------------

2.0.17 (2019-04-12)
-------------------

2.0.16 (2019-04-12)
-------------------

2.0.15 (2019-04-05)
-------------------
* Merge branch 'wrist_current_control' into 'erbium-devel'
  Add missing effort config files
  See merge request robots/tiago_robot!70
* Add missing effort config files
* Contributors: Adria Roig, Hilario Tome

2.0.14 (2019-04-03)
-------------------

2.0.13 (2019-03-28)
-------------------

2.0.12 (2019-03-26)
-------------------
* Merge branch 'incorrect_arm_constraints' into 'erbium-devel'
  Fix wrong constraints on arm joint traj controllers
  See merge request robots/tiago_robot!73
* Fix wrong constraints on arm joint traj controllers
* Contributors: Victor Lopez

2.0.11 (2019-03-26)
-------------------

2.0.10 (2019-03-26)
-------------------

2.0.9 (2019-03-22)
------------------

2.0.8 (2019-03-15)
------------------
* Merge branch 'minor-fixes' into 'erbium-devel'
  Minor fixes
  See merge request robots/tiago_robot!72
* Remove unuesd home_gripper script
* Contributors: Victor Lopez

2.0.7 (2019-03-14)
------------------
* Merge branch 'actuator_simulation' into 'erbium-devel'
  added more paramater to actuators
  See merge request robots/tiago_robot!71
* removed empty spaces
* fixed reduction ratio
* added more paramater to actuators
* Contributors: Hilario Tome

2.0.6 (2019-03-12)
------------------

2.0.5 (2019-02-26)
------------------

2.0.4 (2019-02-08)
------------------

2.0.3 (2019-02-05)
------------------

2.0.2 (2018-12-21)
------------------

2.0.1 (2018-12-20)
------------------

2.0.0 (2018-12-19)
------------------
* Merge branch 'specifics-refactor' into 'erbium-devel'
  Generate automatically play_motion and approach_planner configs
  See merge request robots/tiago_robot!65
* Remove deprecated files
* fixes
* Create configurations of gravity_compensation_with_controller_wrist
* More refactor
* Add head and migrate controller launch
* 1.0.23
* changelog
* Contributors: Procópio Stein, Victor Lopez

1.0.23 (2018-12-05)
-------------------

1.0.22 (2018-12-04)
-------------------
* Merge branch 'as_disable_safety' into 'erbium-devel'
  Disable joint safety by default.
  See merge request robots/tiago_robot!64
* Disable joint safety by default.
* Contributors: alexandersherikov

1.0.21 (2018-11-29)
-------------------
* Merge branch 'as_safety' into 'erbium-devel'
  New joint safety parameters, add missing exec dependencies
  See merge request robots/tiago_robot!63
* Add dependency on pal_local_joint_control.
* New joint safety parameters, add missing exec dependencies
* Contributors: alexandersherikov

1.0.20 (2018-11-19)
-------------------

1.0.19 (2018-10-23)
-------------------

1.0.18 (2018-09-19)
-------------------

1.0.17 (2018-09-17)
-------------------

1.0.16 (2018-08-06)
-------------------

1.0.15 (2018-08-06)
-------------------

1.0.14 (2018-08-01)
-------------------

1.0.13 (2018-08-01)
-------------------

1.0.12 (2018-07-30)
-------------------

1.0.11 (2018-07-13)
-------------------
* Add missing simple_grasping_action dependency for hey5 launch
* Contributors: Victor Lopez

1.0.10 (2018-07-10)
-------------------
* Merge branch 'no_control' into 'erbium-devel'
  No control
  See merge request robots/tiago_robot!52
* Add no control local params for torso
* Add no control local config files
* Contributors: Adrià Roig, Hilario Tome

1.0.9 (2018-05-24)
------------------
* Merge branch 'model_utils' into 'erbium-devel'
  refactoring local joint control
  See merge request robots/tiago_robot!51
* working gravity compensation on robot after pal_local_joint control refactor
* refactoring local joint control
* Contributors: Hilario Tome

1.0.8 (2018-05-02)
------------------

1.0.7 (2018-05-02)
------------------
* Merge branch 'iron-config' into 'erbium-devel'
  Remove arm controllers for Tiago Iron
  See merge request robots/tiago_robot!49
* Remove arm controllers for Tiago Iron
* Merge branch 'remove-chessboard' into 'erbium-devel'
  Remove chessboard, it's a separate entity now
  See merge request robots/tiago_robot!47
* Remove chessboard, it's a separate entity now
* Contributors: Hilario Tome, Victor Lopez, davidfernandez

1.0.6 (2018-04-10)
------------------
* Merge branch 'extra-joints-torque-state-controller' into 'erbium-devel'
  Use extra joints on torque_state_controller
  See merge request robots/tiago_robot!41
* Use extra joints on torque_state_controller
* Contributors: Hilario Tome, Victor Lopez

1.0.5 (2018-03-29)
------------------
* Add new extra joints
* Contributors: Jordan Palacios

1.0.4 (2018-03-26)
------------------
* Merge branch 'recover-chessboard-tiago' into 'erbium-devel'
  Recover chessboard tiago
  See merge request robots/tiago_robot!38
* Revert "remove unused files"
  This reverts commit e50aca81d55736b99e108bb90d681862be39c028.
* Merge branch 'wbc-erbium' into 'erbium-devel'
  WBC erbium
  See merge request robots/tiago_robot!37
* Remove unnecessary launch file
* Contributors: Adria Roig, Jordi Pages, Victor Lopez

1.0.3 (2018-03-16)
------------------
* fixed typo in local joint control, commented out rpc
* Contributors: Hilario Tome

1.0.2 (2018-03-06)
------------------
* Publish_cmd to true, and deprecate publish_wheel_data
* Contributors: Victor Lopez

1.0.1 (2018-02-22)
------------------
* Add gravity_compensation_controller as run depend
* Contributors: Adria Roig

1.0.0 (2018-02-21)
------------------
* changed scaling gains to one for direct effort control
* Fix gravity compensation issues
* added more configuration files for local joint control
* Contributors: Adria Roig, Hilario Tome

0.0.46 (2018-02-20)
-------------------
* added extra wbc controller to mode blacklist and started to add local joint control configuration files
* removed wbc loading from titanium and steel controller launch files
* Contributors: Hilario Tome

0.0.45 (2018-02-08)
-------------------

0.0.44 (2018-02-06)
-------------------

0.0.43 (2018-01-24)
-------------------
* include launch file now in pal_gripper package
* remove no longer needed installation rule
* remove unused files
* Contributors: Jordi Pages

0.0.42 (2017-12-01)
-------------------
* added publish odom option in controller yaml
* Contributors: Procópio Stein

0.0.41 (2017-10-31)
-------------------

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
