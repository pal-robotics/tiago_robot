^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Changelog for package tiago_controller_configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

4.22.0 (2025-10-29)
-------------------
* Merge branch 'tpe/add_open_loop' into 'humble-devel'
  Add openloop to controllers
  See merge request robots/tiago_robot!361
* Add openloop to controllers + remove impedance controller
* Contributors: thomas.peyrucain, thomaspeyrucain

4.21.0 (2025-10-27)
-------------------

4.20.0 (2025-10-20)
-------------------
* Force to current conversion is now handled at actuator level
  Set most motor constants and reducers to 1.0 so the effort to current
  conversion can be handled at actuator level
* Contributors: Jordan Palacios

4.19.6 (2025-10-01)
-------------------
* Remove joint 5 in the gravity compensation due to motor issue
* Contributors: thomas.peyrucain

4.19.5 (2025-09-16)
-------------------

4.19.4 (2025-08-18)
-------------------

4.19.3 (2025-07-16)
-------------------

4.19.2 (2025-07-09)
-------------------

4.19.1 (2025-07-09)
-------------------

4.19.0 (2025-07-08)
-------------------

4.18.0 (2025-06-18)
-------------------

4.17.2 (2025-06-05)
-------------------

4.17.1 (2025-05-13)
-------------------

4.17.0 (2025-04-09)
-------------------
* Standarized gravity comp launcher
* Added command interface param needed for new version of gravity comp
* Contributors: oscarmartinez

4.16.0 (2025-04-03)
-------------------

4.15.1 (2025-03-28)
-------------------

4.15.0 (2025-03-25)
-------------------
* Remove imu broadcaster dependency
* Contributors: Noel Jimenez

4.14.1 (2025-03-18)
-------------------
* Remove unused imu broadcaster
* Contributors: Noel Jimenez

4.14.0 (2025-02-24)
-------------------

4.13.0 (2025-01-22)
-------------------

4.12.0 (2025-01-20)
-------------------

4.11.1 (2025-01-10)
-------------------

4.11.0 (2024-12-16)
-------------------

4.10.0 (2024-11-29)
-------------------
* lunch the gravity comp controller only if not a public simulation and if Tiago has a arm
* Contributors: matteovillani

4.9.0 (2024-11-21)
------------------

4.8.0 (2024-11-21)
------------------

4.7.1 (2024-11-08)
------------------

4.7.0 (2024-11-06)
------------------
* Set update_rate for joint_state_broadcaster
* Contributors: Noel Jimenez

4.6.0 (2024-09-18)
------------------

4.5.0 (2024-08-29)
------------------
* Use launch file directly from base controller_configuration
* Don't load gravity compensation in public sim
* Contributors: David ter Kuile

4.4.0 (2024-08-22)
------------------
* Fix flake8
* Add gravity compensation support for all grippers + improve launch file
* Fix rebase issues + add arm_motor_model to module
* Add dependencies and parameter for motor_model
* Add gravity compensation controller as default controller loaded inactive
* gravity compensation controller loaded in the default controllers
* Contributors: Aina, ileniaperrella, thomas.peyrucain

4.3.0 (2024-08-07)
------------------
* Use controller_type from the controllers config
* Contributors: Noel Jimenez

4.2.21 (2024-08-05)
-------------------
* enable odom tf for pmb2 for public sim
* Contributors: David ter Kuile

4.2.20 (2024-07-29)
-------------------
* Adding open_loop_control variable to head controller
* Contributors: vivianamorlando

4.2.19 (2024-07-25)
-------------------
* Change parameter to arm_type
* Contributors: thomas.peyrucain

4.2.18 (2024-07-09)
-------------------
* Add warning for pal_module_cmake not found
* Contributors: Noel Jimenez

4.2.17 (2024-07-08)
-------------------
* change module name into 10\_*
* change the bases config file for their packages config files
* Contributors: Aina

4.2.16 (2024-06-28)
-------------------
* Add imu sensor broadcaster
* Contributors: davidterkuile

4.2.15 (2024-06-26)
-------------------
* Merge branch 'dtk/move-robot-args' into 'humble-devel'
  Change imports for robot arguments
  See merge request robots/tiago_robot!297
* Change imports for robot arguments
* Contributors: David ter Kuile, davidterkuile

4.2.14 (2024-06-25)
-------------------
* Merge branch 'dtk/fix/base-urdf' into 'humble-devel'
  Dtk/fix/base urdf
  See merge request robots/tiago_robot!295
* Add imu gazebo plugin and imu sensor broadcaster
* Move ros2 control gazebo
* Merge branch 'fix/remove_pmb2_extra_joints' into 'humble-devel'
  Remove casters and suspension from joint_state_broadcaster
  See merge request robots/tiago_robot!296
* Remove casters and suspension from joint_state_broadcaster
* Contributors: David ter Kuile, Jordan Palacios, Noel Jimenez, davidterkuile

4.2.13 (2024-06-05)
-------------------
* Merge branch 'feat/motions' into 'humble-devel'
  pre-recorded_motions
  See merge request robots/tiago_robot!292
* fix launch ee_controller when no-ft-sensor
* Contributors: Aina, davidterkuile

4.2.12 (2024-05-10)
-------------------

4.2.11 (2024-05-09)
-------------------

4.2.10 (2024-05-09)
-------------------

4.2.9 (2024-05-07)
------------------

4.2.8 (2024-04-30)
------------------
* Merge branch 'omm/fix/urdf_complete_std' into 'humble-devel'
  URDF std
  See merge request robots/tiago_robot!278
* Suggested changed
* Module, joy config and restored support for tiago dual
* Omni related checks and files
* Suggested changes
* Launch files moved to TIAGo family standard
* Merge branch 'tpe/add_omni_controller' into 'humble-devel'
  Add missing dependency for the omni_base controller
  See merge request robots/tiago_robot!279
* Add missing dependency for the omni_base controller
* Contributors: Oscar, davidterkuile, thomas.peyrucain

4.2.7 (2024-04-22)
------------------
* Merge branch 'sgg/feat/base_type_omni_base' into 'humble-devel'
  Sgg/feat/base type omni base
  See merge request robots/tiago_robot!273
* Fix whitespace
* mobile_base_controller.launch.py
  Handle is_public_sim
* Add param to ctor
* Add use_sim parameter
* Refactor avoiding if to reduce code complexity
* Update new robot argument method
  Update new robot argument
  Update new robot argument
  Remove blank lines
* Launch joint_state_broadcaster depending on the base_type
  Fix syntax
  Remove redundant check
  Remove redundant check
* Fix syntax
* Fix quotes in comparison
* Parameterized mobile base type
* Hardcoded omni_base controller
* Contributors: Sergi Garcia, davidterkuile

4.2.6 (2024-04-16)
------------------
* Merge branch 'feat/ros2-pipelines' into 'humble-devel'
  added public sim config for mobile base controller
  See merge request robots/tiago_robot!274
* cosmetic
* added public sim config for mobile base controller
* Contributors: andreacapodacqua, antoniobrandi

4.2.5 (2024-04-10)
------------------
* Add ros2controlcli dependency
* Contributors: Noel Jimenez

4.2.4 (2024-03-06)
------------------

4.2.3 (2024-02-28)
------------------

4.2.2 (2024-02-02)
------------------

4.2.1 (2024-01-31)
------------------

4.2.0 (2024-01-31)
------------------
* update license year
* added impedance controller configuration
* update gravity compensation controller config
* Remove unused type parameter from controllers configuration
* Contributors: Noel Jimenez, Sai Kishor Kothakota

4.1.2 (2024-01-19)
------------------

4.1.1 (2024-01-19)
------------------
* adding the config files needed for robotiq
* modifying where to find the urdfs for robotiq
* updating the necessary dependencies for robotiq
* Contributors: Aina Irisarri

4.1.0 (2024-01-18)
------------------
* Merge branch 'ros2-tiago-dual' into 'humble-devel'
  Ros2 tiago dual
  See merge request robots/tiago_robot!240
* Remove unused param
* Contributors: David ter Kuile, davidterkuile

4.0.28 (2023-12-22)
-------------------
* adding pal_hey5 as dependency
* removing temporal exception for hey5 gripper
* relocate the pal-hey5 configuration and launch files
* Contributors: Aina Irisarri

4.0.27 (2023-12-18)
-------------------

4.0.26 (2023-12-14)
-------------------

4.0.25 (2023-12-12)
-------------------
* Launch gripper from its controller_configuration package
* Contributors: Aina Irisarri

4.0.24 (2023-12-12)
-------------------
* Bump module names
* Contributors: Noel Jimenez

4.0.23 (2023-12-11)
-------------------
* Remove unused files
* Contributors: Noel Jimenez

4.0.22 (2023-11-22)
-------------------
* Set 'finishes: True' for default_controllers module
* Update cmake_minimum_required version to 3.8
* Cleanup repository
* Contributors: Noel Jimenez

4.0.21 (2023-11-15)
-------------------

4.0.20 (2023-11-14)
-------------------
* Add website tag
* Rename description and controller modules
* Contributors: Noel Jimenez

4.0.19 (2023-11-13)
-------------------

4.0.18 (2023-11-07)
-------------------
* Split bringup module
* Contributors: Noel Jimenez

4.0.17 (2023-10-19)
-------------------
* Use wheels calibration if exists
* Contributors: Noel Jimenez

4.0.16 (2023-09-18)
-------------------

4.0.15 (2023-09-04)
-------------------

4.0.14 (2023-07-20)
-------------------
* Rename FT Sensor
* Fix ft_sensor_controller frame_id parameter
* Add controller for the FT sensor
* Contributors: Noel Jimenez

4.0.13 (2023-07-11)
-------------------
* Remove schunk wsg option
* Launch controllers depending on robot arguments
* Contributors: Noel Jimenez

4.0.12 (2023-07-05)
-------------------
* Remove pal flags dependency
* Contributors: Noel Jimenez

4.0.11 (2023-06-28)
-------------------
* fix controllers launcher when there is no end_effector
* Contributors: Noel Jimenez

4.0.10 (2023-06-14)
-------------------

4.0.9 (2023-05-11)
------------------
* remove ros1 commented dependencies
* comment controller dependency
* flake8 fixes
* add conditional dependency and do not launch gravity compensation controller as default
* Spawn gravity compensation controller inactive
* Set gravity compensation controller parameters
* Add gravity compensation controller
* Contributors: Adria Roig, Noel Jimenez

4.0.8 (2023-05-11)
------------------

4.0.7 (2023-04-28)
------------------
* set sim time for gazebo controller_manager
* Contributors: Noel Jimenez

4.0.6 (2023-04-17)
------------------

4.0.5 (2023-03-06)
------------------
* Merge branch 'rm_use_sim_time' into 'humble-devel'
  remove use_sim_time parameter
  See merge request robots/tiago_robot!191
* remove use_sim_time parameter
* Contributors: Jordan Palacios, Noel Jimenez

4.0.4 (2023-03-02)
------------------
* Merge branch 'fix_controllers_config' into 'humble-devel'
  remove initial / from controllers config
  See merge request robots/tiago_robot!190
* remove initial / from controllers config
* Contributors: Jordan Palacios, Noel Jimenez

4.0.3 (2023-02-22)
------------------

4.0.2 (2023-02-08)
------------------

4.0.1 (2022-11-10)
------------------
* Merge branch 'update_license' into 'humble-devel'
  Update license
  See merge request robots/tiago_robot!180
* update license
* Merge branch 'fix_dependency' into 'humble-devel'
  fix buildtool dependency
  See merge request robots/tiago_robot!179
* fix buildtool dependency
* Contributors: Jordan Palacios, Noel Jimenez

4.0.0 (2022-11-08)
------------------
* Merge branch 'cleanup' into 'humble-devel'
  Cleanup package.xml files and rm duplicated launcher
  See merge request robots/tiago_robot!174
* rm duplicated launcher
* update package.xml deps
* Merge branch 'fix_substitution' into 'humble-devel'
  fix end effector substitution
  See merge request robots/tiago_robot!169
* fix end effector substitution
* Merge branch 'default_robot_name' into 'humble-devel'
  Add missing default robot name
  See merge request robots/tiago_robot!168
* add missing default robot name
* Merge branch 'update_copyright' into 'humble-devel'
  update copyright and license
  See merge request robots/tiago_robot!167
* update copyright and license
* Merge branch 'cleanup' into 'humble-devel'
  Cleanup
  See merge request robots/tiago_robot!165
* rm ros1 launchers
* Merge branch 'update_maintainers' into 'humble-devel'
  Update maintainers
  See merge request robots/tiago_robot!163
* update maintainers
* Merge branch 'linters' into 'humble-devel'
  Linters
  See merge request robots/tiago_robot!159
* rm print
* linters
* Merge branch 'launch_refactor' into 'humble-devel'
  launch files refactor
  See merge request robots/tiago_robot!158
* launch files refactor
* Merge branch 'tiago_launcher' into 'galactic-devel'
  Tiago launcher
  See merge request robots/tiago_robot!150
* add todo
* Merge branch 'pal-hey5-ros2' into 'foxy-devel'
  pal-hey5 launch files and config
  See merge request robots/tiago_robot!130
* use tiago_launch_utils
* add pal-gripper launch
* update default controllers launch file
* pal-hey5 launch files and config
* Add basic tests to tiago_controller_configuration
* Add extra joints
* Add use_sim_time to controllers as a workaround for https://github.com/ros-controls/ros2_control/issues/325
* Added new parameters required for joint trajectory controllers
  Also, enabled default controllers
* Lower controller manager to 100hz
* Using joint_state_broadcaster instead of controller
* Increased controller manager update rate to match gazebo's
* Added twist_mux to the tiago bringup
  mobile_base_controller now uses the twist unstamped topic instead
* Use correct namespacing for parameters
* Using controller_manager launch_utils
* Support for pal-gripper end effector
* Now uses launch_pal utils
* Added wrist to arm_controller
* Added arm_controller, no wrists
* Added head_controller
* Added torso_controller
* Added default_controllers with mobile_base and joint_state controllers
* Added gazebo_controller_manager_cfg.yaml
* tiago_controller_configuration readded and migrated to ros2
* Ignoring tiago_bringup and tiago_controller_configuration for now
* Contributors: Jordan Palacios, Noel Jimenez, Noel Jimenez Garcia, Victor Lopez, cescfolch, victor

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
