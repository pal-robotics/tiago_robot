/**:
  ros__parameters:
@[if end_effector == "pal-hey5"]@
    controllers: [arm_controller, head_controller, torso_controller, hand_controller]
@[end if]@
@[if end_effector in ["pal-gripper", "robotiq-2f-85", "robotiq-2f-140"]]@
    controllers: [arm_controller, head_controller, torso_controller, gripper_controller]
@[end if]@
@[if end_effector == "custom"]@
    controllers: [arm_controller, head_controller, torso_controller]
@[end if]@
@[if not has_arm]@
    controllers: [head_controller, torso_controller]
@[end if]
    motions:
@[if has_arm]@
@[if end_effector == "pal-gripper"]@
      close:
        joints: [gripper_left_finger_joint, gripper_right_finger_joint]
        positions: [0.0, 0.0]
        times_from_start: [0.5]
        meta:
          name: Close Gripper
          usage: demo
          description: 'Close Gripper'

      close_half:
        joints: [gripper_left_finger_joint, gripper_right_finger_joint]
        positions: [0.024, 0.024]
        times_from_start: [0.5]
        meta:
          name: Close Gripper Half
          usage: demo
          description: 'Close Gripper Halfway'

      open:
        joints: [gripper_left_finger_joint, gripper_right_finger_joint]
        positions: [0.044, 0.044]
        times_from_start: [0.5]
        meta:
          name: Open Gripper
          usage: demo
          description: 'Open Gripper'

      point:
        joints: [gripper_left_finger_joint, gripper_right_finger_joint]
        positions: [0.0, 0.0]
        times_from_start: [0.5]
        meta:
          name: Point Gripper Pose
          usage: demo
          description: 'Close Gripper to point to something'
@[end if]@
@[if end_effector == "pal-hey5"]@
      open:
        joints: [hand_thumb_joint, hand_index_joint, hand_mrl_joint]
        positions: [-1.0, -1.0, -1.0,
                    0.0, 0.0, 0.0]
        times_from_start: [0.1, 2.5]
        meta:
          name: Open Hand
          usage: demo
          description: 'Opens hand'

      close:
        joints: [hand_thumb_joint, hand_index_joint, hand_mrl_joint]
        positions: [2.37, 0.0, 0.0,
                    6.2, 6.8, 9.2]
        times_from_start: [0.1, 2.5]
        meta:
          name: Close Hand
          usage: demo
          description: 'Closes hand'

      close_half:
        joints: [hand_thumb_joint, hand_index_joint, hand_mrl_joint]
        positions: [3.2, 3.8, 4.6]
        times_from_start: [2.5]
        meta:
          name: Close Hand Half
          usage: demo
          description: 'Closes hand halfway'

      point:
        joints: [hand_thumb_joint, hand_index_joint, hand_mrl_joint]
        positions: [2.37, -1.0, 0.0,
                    6.2, 0.0, 9.2]
        times_from_start: [0.1, 1.5]
        meta:
          name: Pointing Hand
          usage: demo
          description: 'Pointing Hand'

      thumb_up_hand:
        joints: [hand_thumb_joint, hand_index_joint, hand_mrl_joint]
        positions: [-1.0, 0.0, 0.0,
                    0.0, 6.8, 9.2]
        times_from_start: [0.1, 1.5]
        meta:
          name: Thumb Up Hand
          usage: demo
          description: 'thumb_up_hand'

      pinch_hand:
        joints: [hand_thumb_joint, hand_index_joint, hand_mrl_joint]
        positions: [0.0, -1.0, -1.0,
                    3.37, 4.0, 0.0]
        times_from_start: [0.1, 1.5]
        meta:
          name: Pinch Hand
          usage: demo
          description: 'pinch_hand'
@[end if]@
@[if end_effector in ["robotiq-2f-85", "robotiq-2f-140"]]@
      close:
        joints: [gripper_finger_joint]
        positions: [@[if end_effector == "robotiq-2f-85"]0.8@[else]0.7@[end if]]
        times_from_start: [0.5]
        meta:
          name: Close Gripper
          usage: demo
          description: 'Closes gripper'

      close_half:
        joints: [gripper_finger_joint]
        positions: [@[if end_effector == "robotiq-2f-85"]0.4@[else]0.35@[end if]]
        times_from_start: [0.5]
        meta:
          name: Close Gripper Half
          usage: demo
          description: 'Closes gripper halfway'

      open:
        joints: [gripper_finger_joint]
        positions: [0.0]
        times_from_start: [0.5]
        meta:
          name: Open Gripper
          usage: demo
          description: 'Open gripper'

      point:
        joints: [gripper_finger_joint]
        positions: [@[if end_effector == "robotiq-2f-85"]0.8@[else]0.7@[end if]]
        times_from_start: [0.5]
        meta:
          name: Point
          usage: demo
          description: 'Closes gripper to point to something'
@[end if]@
@[else]@
      home:
        joints: [torso_lift_joint]
        positions: [0.15]
        times_from_start: [3.0]
        meta:
          name: Home
          usage: demo
          description: 'Go home'

      head_tour:
        joints: [head_1_joint, head_2_joint]
        positions: [0.0, 0.0,
                    0.7, 0.0,
                    0.7, 0.3,
                    0.7, -0.3,
                    0.7, 0.3,
                    -0.7, 0.3,
                    -0.7, -0.3,
                    0.0, 0.0]
        times_from_start: [0.1, 3.0, 6.0, 9.0, 12.0, 15.0, 18.0, 21.0]
        meta:
          name: Head Tour
          usage: demo
          description: 'head_tour'

      inspect_surroundings:
        joints: ['head_1_joint', 'head_2_joint']
        positions: [-1., -0.85,
                    -1., -0.85,
                    1., -0.85,
                    1., -0.85,
                    0., -0.85]
        times_from_start: [1.5, 2.0, 4.5, 5.0, 7.0]
        meta:
          name: Inspect Surroundings
          usage: demo
          description: 'Inspect surroundings around the robot'
@[end if]@


