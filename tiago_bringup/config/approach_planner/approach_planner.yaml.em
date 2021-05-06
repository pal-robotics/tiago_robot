disable_motion_planning: false
approach_planner:
  planning_groups: # Sorted by order of preference
@[if has_arm]@
    - arm_torso
    - arm
@[else]@
    - torso
@[end if]@
  exclude_from_planning_joints:
    - head_1_joint
    - head_2_joint
@[if end_effector == "pal-hey5"]@
    - hand_thumb_joint
    - hand_mrl_joint
    - hand_index_joint
@[end if]@
@[if end_effector == "pal-gripper"]@
    - gripper_left_finger_joint
    - gripper_right_finger_joint
@[end if]@
@[if end_effector in ["schunk-wsg", "robotiq-2f-85", "robotiq-2f-140"]]@
    - gripper_finger_joint
@[end if]@
  joint_tolerance: 0.01
  skip_planning_approach_vel: 0.5
  skip_planning_approach_min_dur: 0.5
