from launch import LaunchDescription
from launch_ros.actions import Node

from tiago_description.tiago_launch_utils import (get_tiago_hw_arguments,
                                                  generate_robot_description_action)


def generate_launch_description():
    parameters = {'robot_description': generate_robot_description_action()}

    rsp = Node(package='robot_state_publisher',
               executable='robot_state_publisher',
               output='both',
               parameters=[parameters])

    tiago_args = get_tiago_hw_arguments(
        laser_model=True,
        arm=True,
        end_effector=True,
        ft_sensor=True,
        camera_model=True,
        default_laser_model="sick-571")

    return LaunchDescription([*tiago_args, rsp])
