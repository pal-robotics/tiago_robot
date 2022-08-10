^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Changelog for package tiago_description
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

2.3.7 (2022-08-10)
------------------
* Merge branch 'fix_torso_collision' into 'erbium-devel'
  Fix collision boxes for the torso
  See merge request robots/tiago_robot!156
* Fix collision boxes for the torso
* Contributors: saikishor, thomaspeyrucain

2.3.6 (2022-08-04)
------------------

2.3.5 (2022-07-26)
------------------

2.3.4 (2022-07-21)
------------------

2.3.3 (2022-07-19)
------------------

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
* Merge branch 'no-end-effector-bugfix' of gitlab:robots/tiago_robot into no-end-effector-bugfix
* Apply 5 suggestion(s) to 4 file(s)
* remove redundant spaces
* remove redundant spaces
* end effector back to hey-5
* prevent ft sensor to load when no arm is attached
* add epick end-effector
* add no-ee to urdf
* update motions config file
* fix faulty if statement in urdf
* Update eval function, generate scripts
* add no-ee to urdf
* edit motions config
* update motions config file
* fix faulty if statement in urdf
* made some changes
* Update eval function, generate scripts
* prevent ft sensor to load when no arm is attached
* add epick end-effector
* add no-ee to urdf
* update motions config file
* fix faulty if statement in urdf
* Update eval function, generate scripts
* add no-ee to urdf
* edit motions config
* update motions config file
* fix faulty if statement in urdf
* made some changes
* Update eval function, generate scripts
* add epick end-effector
* add no-ee to urdf
* edit motions config
* update motions config file
* fix faulty if statement in urdf
* made some changes
* Update eval function, generate scripts
* add no-ee to urdf
* edit motions config
* update motions config file
* fix faulty if statement in urdf
* made some changes
* Update eval function, generate scripts
* Contributors: David ter Kuile, saikishor

2.2.14 (2022-04-20)
-------------------
* Fix materials
* Contributors: Giang Nguyen

2.2.13 (2022-03-23)
-------------------
* Merge branch 'fix_home_robotiq_2f_140' into 'erbium-devel'
  Fix home position for robotiq-2f-140 + fix Reach max out of range motion + add effort_controller
  See merge request robots/tiago_robot!148
* Add pal_robotiq_epick_description dependency on tiago_description package
* Contributors: saikishor, thomaspeyrucain

2.2.12 (2022-03-18)
-------------------
* Added the robotiq epick to the rostests
* Contributors: Sai Kishor Kothakota

2.2.11 (2022-03-18)
-------------------
* Merge branch 'add_robotiq_epick_gripper' into 'erbium-devel'
  Add link to epick urdf
  See merge request robots/tiago_robot!145
* Match the code with the other robotiq gripper
* add prefix parameter
* Add link to epick urdf
* Contributors: saikishor, thomaspeyrucain

2.2.10 (2022-02-22)
-------------------

2.2.9 (2022-01-19)
------------------

2.2.8 (2021-12-22)
------------------

2.2.7 (2021-11-25)
------------------
* Merge branch 'omnibase-gravity-fix' into 'erbium-devel'
  changing ros_planar_move gazebo plugin with ros_force_based_move in order to preserve gravity
  See merge request robots/tiago_robot!143
* Moved force_based_move AFTER ros_control
* Changed the order of the plugin in order to make the wheel rotating correctly
* Add dependency to the hector gazebo plugin for the omni base simulation
* Removing the needs for a duplicated gazebo.urdf file
* Removed dependencies
* changing ros_planar_move gazebo plugin with ros_force_based_move in order to preserve gravity
* Contributors: antoniobrandi, saikishor

2.2.6 (2021-11-22)
------------------

2.2.5 (2021-11-19)
------------------
* Merge branch 'fix_arm_1_collision_mesh' into 'erbium-devel'
  fix the arm_1_link collision mesh which is causing troubles in capsule_decomposition generation
  See merge request robots/tiago_robot!141
* fix the arm_1_link collision mesh which is causing troubles in capsule_decomposition generation
* Merge branch 'conditional_dependencies' into 'erbium-devel'
  Conditional dependencies
  See merge request robots/tiago_robot!140
* added PAL_DISTRO conditioning for PAL dependencies
* change to package version 3
* Contributors: Sai Kishor Kothakota, victor

2.2.4 (2021-11-10)
------------------

2.2.3 (2021-11-10)
------------------

2.2.2 (2021-11-09)
------------------

2.2.1 (2021-11-09)
------------------

2.2.0 (2021-11-03)
------------------
* Merge branch 'omni_base_robot' into 'erbium-devel'
  Omni base robot
  See merge request robots/tiago_robot!137
* preparing configuration for a tiago with omni base
* Creating tiago with omni_base robot
* Contributors: antoniobrandi, saikishor

2.1.5 (2021-09-22)
------------------

2.1.4 (2021-08-31)
------------------

2.1.3 (2021-08-06)
------------------

2.1.2 (2021-07-16)
------------------
* Merge branch 'fix_inertia_matrices' into 'erbium-devel'
  fix the inertia matrices of arm_tool_link and of force torque sensor
  See merge request robots/tiago_robot!129
* fix the inertia matrices of arm_tool_link and of force torque sensor
* Merge branch 'update-apache-licence-2021' into 'erbium-devel'
  Updating apache License 2021
  See merge request robots/tiago_robot!128
* Updating apache License
* Contributors: Sai Kishor Kothakota, ThomasPeyrucain, saikishor, victor

2.1.1 (2021-06-01)
------------------
* Merge branch 'parametrize-robot-description' into 'erbium-devel'
  Parametrize robot_description param name
  See merge request robots/tiago_robot!127
* Parametrize robot_description param name
* Contributors: Victor Lopez, victor

2.1.0 (2021-05-06)
------------------
* Merge branch 'robotiq_gripper' into 'erbium-devel'
  Robotiq gripper
  See merge request robots/tiago_robot!125
* add robotiq dependencies and robotiq grippers to the tests
* update the robotiq end effector naming
* integrate the new robotiq-85 and robotiq-140 grippers
* Contributors: Sai Kishor Kothakota, saikishor

2.0.58 (2021-04-09)
-------------------

2.0.57 (2021-03-19)
-------------------
* Merge branch 'custom-end-effector-dual' into 'erbium-devel'
  Custom end effector dual
  See merge request robots/tiago_robot!123
* fix: logic loading custom ee urdf from tiago_robot
* fix: load custom urdfs
* fix: treat string as binary always entering to dual if
* fix: duplicating right ee causing error link
* fix: xacro negation
* Contributors: daniellopez, victor

2.0.56 (2021-03-01)
-------------------
* Merge branch 'fix_left_arm_tiago_dual_com' into 'erbium-devel'
  Add reflect for 4th link CoM
  See merge request robots/tiago_robot!122
* Add reflect for 4th link CoM
* Contributors: Luca Marchionni, victor

2.0.55 (2021-01-15)
-------------------
* Merge branch 'gravity_compensation_fix' into 'erbium-devel'
  Update arm_3_link weight for gravity compensation
  See merge request robots/tiago_robot!120
* Update arm_3_link weight for gravity compensation
* Contributors: Adria Roig, victor

2.0.54 (2020-09-08)
-------------------
* Merge branch 'no_safety_eps_head' into 'erbium-devel'
  added no safety eps to head
  See merge request robots/tiago_robot!119
* fix the no_safety_epc head macro issue
* added no safety eps to head
* Merge branch 'new-endoscopic-dual' of gitlab:robots/tiago_robot into new-endoscopic-dual
* Contributors: Sai Kishor Kothakota, daniellopez, victor

2.0.53 (2020-07-30)
-------------------

2.0.52 (2020-07-27)
-------------------

2.0.51 (2020-07-15)
-------------------
* Merge branch 'fix-head-calibration' into 'erbium-devel'
  add eps to head_motor_2 head.urdf.xacro
  See merge request robots/tiago_robot!116
* add eps to head_motor_2 head.urdf.xacro
* Contributors: daniellopez, victor

2.0.50 (2020-07-10)
-------------------
* Merge branch 'add-no-safety-eps' into 'erbium-devel'
  Add the option of disabling arm_safety_eps via launch file
  See merge request robots/tiago_robot!115
* Fix default no_safety_eps value
* Add the option of disabling arm_safety_eps via launch file
* Contributors: Victor Lopez, victor

2.0.49 (2020-07-01)
-------------------
* Merge branch 'add-master-calibration' into 'erbium-devel'
  Add master calibration compatibility for eye hand and extrinsic
  See merge request robots/tiago_robot!114
* Proper pal_camera_calibration_extrinsics path
* Add master calibration compatibility for eye hand and extrinsic
* Contributors: Victor Lopez, victor

2.0.48 (2020-06-10)
-------------------
* Merge branch 'gravity-compensation' into 'erbium-devel'
  change values to have a better gravity compensation. Not optimum result for all tiagos found
  See merge request robots/tiago_robot!113
* change values to have a better gravity compensation. Not optimum result for all tiagos found
* Contributors: daniellopez, victor

2.0.47 (2020-05-15)
-------------------
* Merge branch 'wrist-2017' into 'erbium-devel'
  adjust mass of wrist-2017
  See merge request robots/tiago_robot!112
* adjust mass of wrist-2017
* Contributors: YueErro, victor

2.0.46 (2020-05-13)
-------------------
* Merge branch 'wrist-2019' into 'erbium-devel'
  Use mass and inertia values based on the wrist type
  See merge request robots/tiago_robot!111
* Use mass and inertia values based on the wrist type
* Contributors: Sai Kishor Kothakota, victor

2.0.45 (2020-05-12)
-------------------
* Merge branch 'remove_default_parsed_package' into 'erbium-devel'
  remove default description_calibration_package argument in head
  See merge request robots/tiago_robot!110
* Merge branch 'no_arm' into 'erbium-devel'
  fix wrong_wrist_model condition
  See merge request robots/tiago_robot!107
* fix wrong_wrist_model condition
* remove default description_calibration_package argument in head
* Contributors: saikishor, victor, yueerro

2.0.44 (2020-05-12)
-------------------
* Merge branch 'description-calibration-fixes' into 'erbium-devel'
  Description calibration fixes
  See merge request robots/tiago_robot!109
* parse package name instead of individual elements and load files respective to package
* pass the camera origin as an argument to head
* Contributors: Sai Kishor Kothakota, victor

2.0.43 (2020-05-08)
-------------------
* Fix mesh orientation
* Merge branch 'fix-orbbec-astra' into 'erbium-devel'
  Fix frames for orbbec astra
  See merge request robots/tiago_robot!108
* depth frame for orbbec is referenced on the rgb frame
* Fix y orientation error
* Fix frames for orbbec astra
* Remove unused properties
* Contributors: Victor Lopez, victor

2.0.42 (2020-05-07)
-------------------
* Use different meshes for wrist 2017
* Contributors: Victor Lopez

2.0.41 (2020-05-07)
-------------------
* Adjust end_effector-wrist distance without FT sensor
* Contributors: Victor Lopez

2.0.40 (2020-05-06)
-------------------
* Merge branch 'fix-tiago-wrist-offset' into 'erbium-devel'
  Change wrist tool link position with wrist 2017
  See merge request robots/tiago_robot!106
* Change wrist tool link position with wrist 2017
* Contributors: Victor Lopez, victor

2.0.39 (2020-04-21)
-------------------
* Merge branch 'custom-ee' into 'erbium-devel'
  Allow using custom end-effector
  See merge request robots/tiago_robot!102
* Add test for custom End-Effector
* Allow using custom end-effector
* Contributors: davidfernandez, victor

2.0.38 (2020-02-27)
-------------------

2.0.37 (2020-02-14)
-------------------
* Merge branch 'wrist_model' into 'erbium-devel'
  add wrist_model arg
  See merge request robots/tiago_robot!101
* add wrist_model arg
* Contributors: Victor Lopez, YueErro

2.0.36 (2020-01-28)
-------------------

2.0.35 (2019-11-06)
-------------------
* Merge branch 'arm_offset_fix' into 'erbium-devel'
  parse arm joint offsets through the macro
  See merge request robots/tiago_robot!98
* parse arm joint offsets through the macro
* Contributors: Sai Kishor Kothakota, Victor Lopez

2.0.34 (2019-10-30)
-------------------
* Merge branch 'ivo_robot' into 'erbium-devel'
  parameterize the parsed offsets w.r.t to the name
  See merge request robots/tiago_robot!96
* parameterize the parsed offsets w.r.t to the name
* Contributors: Jordan Palacios, Sai Kishor Kothakota

2.0.33 (2019-10-21)
-------------------

2.0.32 (2019-10-16)
-------------------
* Merge branch 'fix-gazebo-pose-frame' into 'erbium-devel'
  fixed frame used in ground truth pose
  See merge request robots/tiago_robot!95
* fixed frame used in ground truth pose
* Contributors: Procópio Stein

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

2.0.26 (2019-07-18)
-------------------

2.0.25 (2019-07-09)
-------------------

2.0.24 (2019-07-08)
-------------------
* Merge branch 'new-dual-arm-2-limit' into 'erbium-devel'
  Fix dual arm 2 lower limit
  See merge request robots/tiago_robot!88
* Fix dual arm 2 lower limit
* Contributors: Victor Lopez

2.0.23 (2019-06-07)
-------------------

2.0.22 (2019-05-21)
-------------------
* Merge branch 'tiago-dual-arm-1-2' into 'erbium-devel'
  Tiago dual arm 1 2
  See merge request robots/tiago_robot!85
* Fix joint limits for tiago 2 arm
* Fix transmission duplicated name for tiago 2 arm
* Modify arm 1, 2 and 3 for TIAGo Dual
* Merge branch 'melodic_fixes' into 'erbium-devel'
  added boolean false to the variation lists
  See merge request robots/tiago_robot!86
* added boolean false to the variation lists
* Add default parameters to show.launch for easier testing
* Contributors: Sai Kishor Kothakota, Victor Lopez

2.0.21 (2019-05-13)
-------------------

2.0.20 (2019-05-09)
-------------------

2.0.19 (2019-05-02)
-------------------

2.0.18 (2019-04-23)
-------------------
* Merge branch 'reduce-padding' into 'erbium-devel'
  Reduce padding for tiago arm
  See merge request robots/tiago_robot!82
* Reduce padding for tiago arm
* Contributors: Victor Lopez

2.0.17 (2019-04-12)
-------------------
* Merge branch 'tiago-dual' into 'erbium-devel'
  Fixes for tiago dual
  See merge request robots/tiago_robot!80
* Corrected com positions and some inertias
* Merge remote-tracking branch 'origin/urdf_arm_review' into tiago-dual
* Fix changed orientation of original tiago arm
* Finish dual arm urdf
* Almost finished dual arms
* Fixes for tiago dual
* fix max vel and adjust max efforts
* Fixed torque and speed limits for arm
* review link 4-5-6-7
* Contributors: Jordi Pages, Luca, Victor Lopez

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

2.0.11 (2019-03-26)
-------------------
* Fix wrong include, could be duplicated
* Contributors: Victor Lopez

2.0.10 (2019-03-26)
-------------------
* Merge branch 'move-end-effector-xacro' into 'erbium-devel'
  Move end_effector xacro code for reusing
  See merge request robots/tiago_robot!75
* Fix xacro warnings
* Parametrize arm origin
* Move end_effector xacro code for reusing
* Contributors: Victor Lopez

2.0.9 (2019-03-22)
------------------
* Merge branch 'fix_xacro_warning2' into 'erbium-devel'
  Fix xacro warning2
  See merge request robots/tiago_robot!45
* fix xacro deprecation warning
* Contributors: Jeremie Deray, Procópio Stein

2.0.8 (2019-03-15)
------------------

2.0.7 (2019-03-14)
------------------

2.0.6 (2019-03-12)
------------------
* Add padding and extend blacklist
* Contributors: Victor Lopez

2.0.5 (2019-02-26)
------------------
* Merge branch 'multi_simulation' into 'erbium-devel'
  Fix multitiago simulation
  See merge request robots/tiago_robot!69
* Fix multitiago simulation
* Contributors: Victor Lopez, davidfernandez

2.0.4 (2019-02-08)
------------------
* Merge branch 'camera_calib' into 'erbium-devel'
  added extrinsic camera calibration file modifications
  See merge request robots/tiago_robot!68
* added extrinsic camera calibration file changes
* Contributors: Jordi Pages, Sai Kishor Kothakota

2.0.3 (2019-02-05)
------------------
* Remove usages of pass_all_args, not supported in kinetic yet
* Contributors: Victor Lopez

2.0.2 (2018-12-21)
------------------

2.0.1 (2018-12-20)
------------------

2.0.0 (2018-12-19)
------------------
* Merge branch 'specifics-refactor' into 'erbium-devel'
  Generate automatically play_motion and approach_planner configs
  See merge request robots/tiago_robot!65
* Add default params to upload.launch
* Fix arguments for upload
* Add head and migrate controller launch
* Parametrize urdf
* remove deprecated launch file
* 1.0.23
* changelog
* Contributors: Procópio Stein, Victor Lopez

1.0.23 (2018-12-05)
-------------------

1.0.22 (2018-12-04)
-------------------

1.0.21 (2018-11-29)
-------------------

1.0.20 (2018-11-19)
-------------------
* Merge branch 'add-grasping-motions' into 'erbium-devel'
  Add motions for pal grasping pipeline
  See merge request robots/tiago_robot!62
* Add new motions for grasping
* Add collision parameters for tiago
* Contributors: Victor Lopez

1.0.19 (2018-10-23)
-------------------

1.0.18 (2018-09-19)
-------------------

1.0.17 (2018-09-17)
-------------------

1.0.16 (2018-08-06)
-------------------
* Merge branch 'multiple-link-collisions' into 'erbium-devel'
  Split torso collision into multiple elements for better convex hulls
  See merge request robots/tiago_robot!56
* Split torso collision into multiple elements for better convex hulls
* Contributors: Hilario Tome, Victor Lopez

1.0.15 (2018-08-06)
-------------------
* Merge branch 'add-collision-parameters' into 'erbium-devel'
  Add collision_parameters.yaml
  See merge request robots/tiago_robot!57
* Add collision_parameters.yaml
* Contributors: Hilario Tome, Victor Lopez

1.0.14 (2018-08-01)
-------------------

1.0.13 (2018-08-01)
-------------------

1.0.12 (2018-07-30)
-------------------
* Merge branch 'fix-simulation-warnings' into 'erbium-devel'
  Fix simulation warnings
  See merge request robots/tiago_robot!54
* remove gazebo property overwrite
* fix typo in comment
* call xacro rather than xacro.py
* Contributors: Jordi Pages, Victor Lopez

1.0.11 (2018-07-13)
-------------------

1.0.10 (2018-07-10)
-------------------

1.0.9 (2018-05-24)
------------------

1.0.8 (2018-05-02)
------------------
* Merge branch 'deprecate_upload_tiago' into 'erbium-devel'
  deprecate upload_tiago & fix xacro warning --inorder
  See merge request robots/tiago_robot!42
* deprecate upload_tiago & fix xacro warning --inorder
* Contributors: Hilario Tome, Jeremie Deray

1.0.7 (2018-05-02)
------------------
* Merge branch 'mr-origin-43' into 'erbium-devel'
  normalize xmlns across xacro files
  See merge request robots/tiago_robot!48
* normalize xmlns across xacro files
* Merge branch 'remove-chessboard' into 'erbium-devel'
  Remove chessboard, it's a separate entity now
  See merge request robots/tiago_robot!47
* Remove chessboard, it's a separate entity now
* Merge branch 'fix_xacro_warning' into 'erbium-devel'
  fix xacro warning
  See merge request robots/tiago_robot!44
* fix xacro warning
  deprecated: xacro tags should be prepended with 'xacro' xml namespace.
  Use the following script to fix incorrect usage:
  find . -iname "*.xacro" | xargs sed -i 's#<\([/]\?\)\(if\|unless\|include\|arg\|property\|macro\|insert_block\)#<\1xacro:\2#g'
* Contributors: Hilario Tome, Jeremie Deray, Victor Lopez

1.0.6 (2018-04-10)
------------------

1.0.5 (2018-03-29)
------------------

1.0.4 (2018-03-26)
------------------
* Merge branch 'recover-chessboard-tiago' into 'erbium-devel'
  Recover chessboard tiago
  See merge request robots/tiago_robot!38
* Increase camera FoV, more similar to real robot
* Improve chessboard position wrt real robot
* Add missing tiago_steel_chessboard files
* Revert "remove unused files"
  This reverts commit e50aca81d55736b99e108bb90d681862be39c028.
* Contributors: Jordi Pages, Victor Lopez

1.0.3 (2018-03-16)
------------------

1.0.2 (2018-03-06)
------------------
* Merge branch 'add-kinematic-launch' into 'dubnium-devel'
  add launch for kinematic testing
  See merge request robots/tiago_robot!35
  (cherry picked from commit 252410614569a03cf74ec494039981c8d660a834)
  89ebce04 add launch for kinematic testing
* Contributors: Victor Lopez

1.0.1 (2018-02-22)
------------------

1.0.0 (2018-02-21)
------------------
* added joint state interface transmission
* Fix gravity compensation issues
* added more configuration files for local joint control
* Contributors: Adria Roig, Hilario Tome

0.0.46 (2018-02-20)
-------------------

0.0.45 (2018-02-08)
-------------------
* add pal_wsg_gripper_description dependency
* Contributors: Jordi Pages

0.0.44 (2018-02-06)
-------------------
* add fingertip force sensors
* remove blank line
* Contributors: Jordi Pages

0.0.43 (2018-01-24)
-------------------
* add files for schunk-gripper based TIAGo
* remove unused files
* Contributors: Jordi Pages

0.0.42 (2017-12-01)
-------------------
* increase eps in arm and head joints' ranges
  To prevent reaching mechanical limits after eye-hand calibration, which changes the offsets of these joints
* Contributors: Jordi Pages

0.0.41 (2017-10-31)
-------------------
* Merge remote-tracking branch 'origin/automatic_calibration' into dubnium-devel
* deleted the calibration.urdf.xacro from this package and moved to another external package accessible from the customer
* Modify the offset to allow the automatic calibration
* Contributors: AleDF, Hilario Tomé

0.0.40 (2017-10-27)
-------------------
* added support for absolute encoders
* update urdf arm model for CoM position fix
* Add simple tests for URDF files
* Contributors: Hilario Tomé, Luca, davidfernandez

0.0.39 (2017-07-12)
-------------------

0.0.38 (2017-05-16)
-------------------
* Add configurations for Tiago Iron
* Contributors: davidfernandez

0.0.37 (2017-05-05)
-------------------

0.0.36 (2017-04-24)
-------------------
* Allow multiple Tiagos on Gazebo
  Refs #15402
* Contributors: David Fernandez

0.0.35 (2016-12-21)
-------------------

0.0.34 (2016-11-06)
-------------------
* move torso 0 position 1 cm upwards
* Contributors: Jordi Pages

0.0.33 (2016-11-04)
-------------------

0.0.32 (2016-10-26)
-------------------

0.0.31 (2016-10-14)
-------------------
* Added gazebo plugin to simulate the world frame in gazebo
* 0.0.30
* Update changelog
* fixes #14569: proper RGB point clouds
* add myself as maintainer
* add myself as maintainer
* refs #13892: fix reference frame
* 0.0.29
* Update changelog
* 0.0.28
* Update changelog
* 0.0.27
* Update changelog
* 0.0.26
* Update changelog
* 0.0.25
* Update changelog
* Making the simulation be more close to the real robot xtion
* 0.0.24
* changelog
* 0.0.23
* Update changelog
* Add imu to gazebo simulation
* 0.0.22
* Update changelog
* Add provideFeedback to tiago wrist
* 0.0.21
* Update changelog
* 0.0.20
* Update changelog
* 0.0.19
* Update changelog
* 0.0.18
* changelog
* 0.0.17
* changelog
* 0.0.16
* Update changelog
* 0.0.15
* Update changelog
* 0.0.14
* Update changelog
* 0.0.13
* Update changelog
* Merge branch 'dubnium-devel' of gitlab:robots/tiago_robot into dubnium-devel
* Corrected the pose of the gripper
* Contributors: Adria Roig, Jeremie Deray, Jordi Pages, Sam Pfeiffer, Victor Lopez

0.0.30 (2016-10-13)
-------------------
* fixes #14569: proper RGB point clouds
* add myself as maintainer
* add myself as maintainer
* refs #13892: fix reference frame
* Contributors: Jordi Pages

0.0.29 (2016-07-28)
-------------------

0.0.28 (2016-07-28)
-------------------

0.0.27 (2016-07-19)
-------------------

0.0.26 (2016-07-08)
-------------------

0.0.25 (2016-06-28)
-------------------
* Making the simulation be more close to the real robot xtion
* Contributors: Sam Pfeiffer

0.0.24 (2016-06-15)
-------------------

0.0.23 (2016-06-15)
-------------------
* Add imu to gazebo simulation
* Contributors: Sam Pfeiffer

0.0.22 (2016-06-15)
-------------------
* Add provideFeedback to tiago wrist
* Contributors: Victor Lopez

0.0.21 (2016-06-15)
-------------------

0.0.20 (2016-06-14)
-------------------

0.0.19 (2016-06-14)
-------------------

0.0.18 (2016-06-14)
-------------------

0.0.17 (2016-06-13)
-------------------

0.0.16 (2016-06-13)
-------------------

0.0.15 (2016-06-13)
-------------------

0.0.14 (2016-06-10)
-------------------

0.0.13 (2016-06-10)
-------------------
* Merge branch 'dubnium-devel' of gitlab:robots/tiago_robot into dubnium-devel
* Corrected the pose of the gripper
* Contributors: Sam Pfeiffer


0.0.12 (2016-06-07)
-------------------
* Merged changes of wrist range + ft sensor
* Add hardware port of force torque
* Add force torque sensor
* Contributors: Sam Pfeiffer

0.0.11 (2016-06-03)
-------------------
* missing deps pal_gripper
* tiago has sonars
* Remove old gripper references
* Changed previous gripper to newer one
* fixes #13516
* Contributors: Bence Magyar, Hilario Tome, Jeremie Deray, Jordi Pages, Sam Pfeiffer, Victor Lopez, jordi.pages@pal-robotics.com

0.0.10 (2016-04-26)
-------------------

0.0.9 (2016-04-25)
------------------
* Updated joint limits as per errors found by Louis
* Contributors: Sam Pfeiffer

0.0.8 (2016-04-19)
------------------
* fixed rgb_optical_frame name affecting simulation
* fix chessboard pose
* remove collision in calibration chessboard
* Contributors: jordi.pages@pal-robotics.com

0.0.7 (2016-04-11)
------------------
* Update urdf
* Add new meshes
* Delete old meshes
* Contributors: Sam Pfeiffer

0.0.6 (2016-03-31)
------------------
* Fixed wheel sleeping in gazebo, and added head transmission (This can break the real robot if a blacklist is not implemented in pal_ros_control
* Contributors: Hilario Tome

0.0.5 (2016-03-21)
------------------
* Add effort transmision
* using base_sensors instead of base
* remove hey5 hand from URDF
* Added safety controller to torso lift joint
* Update inertial params
* 7 cm / sec torso speed
* Gripper parts color
* Updated gripper base mesh
* Update head, todo: dae coloring for the head_2
* Update license
* Update joint limit
* Remove module-only arm
* Arm 1 collision added
* Update collision & meshes
* Remove old head mesh
* Update torso meshes &  collision
* Update limits
* Add cover for module hole
* Review of joint limits
* Update arm
* Update torso
* Update gripper finger
* No need for have_base_rgdb anymore
* New arm distances, more to come
* Update head distance from torso_lift_link
* Remove temporary cabling boxes
* change torso limits and update motions
* Update gripper length to approx real one
* Update head
* add cover on top of mobile base
  Define collision and visual elements needed for the motion planning of TIAGo proof-of-concept
* restrict lifter joint to go lower than 5 cm
  Take into account new mobile base covers that are 5 cm high
* DarkGrey for all arm parts in gazebo
* Updated limits
* Add cable channel to the front of the column
* Increase speed of torso
* Contributors: Bence Magyar, Hilario Tome, Jordi Pages, Sam Pfeiffer, jordi.pages@pal-robotics.com

0.0.4 (2015-05-20)
------------------
* Add safety box around the hand
* Fix wrist direction
* Add yellow
* Add more collision geometries representing boxes and cable carriers on first tiago
* Update joint limit to real
* Update elbow joint limits
* Update head joint limits
* Adding tiago_shadow, tiago with shadow lite hand (! no dependency on shadow packages on purpose!)
* Add arm with only modules, no wrist
* Contributors: Bence Magyar

0.0.3 (2015-04-15)
------------------

0.0.2 (2015-04-15)
------------------
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
* Change occureces of ant to pmb2
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
