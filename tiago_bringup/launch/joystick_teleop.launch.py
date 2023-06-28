# Copyright (c) 2022 PAL Robotics S.L. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, OpaqueFunction
from launch.conditions import LaunchConfigurationEquals
from launch.substitutions import LaunchConfiguration

from launch_pal.arg_utils import read_launch_argument
from launch_pal.robot_utils import (get_arm,
                                    get_end_effector,
                                    get_ft_sensor,
                                    get_robot_name)
from launch_ros.actions import Node

from tiago_description.tiago_launch_utils import get_tiago_hw_suffix


def declare_args(context, *args, **kwargs):

    robot_name = read_launch_argument('robot_name', context)

    return [get_arm(robot_name),
            get_end_effector(robot_name),
            get_ft_sensor(robot_name)]


def launch_setup(context, *args, **kwargs):

    arm = read_launch_argument('arm', context)
    end_effector = read_launch_argument('end_effector', context)
    ft_sensor = read_launch_argument('ft_sensor', context)

    joy_teleop_path = os.path.join(
        get_package_share_directory('tiago_bringup'), 'config', 'joy_teleop',
        'joy_teleop' + get_tiago_hw_suffix(arm=arm,
                                           end_effector=end_effector,
                                           ft_sensor=ft_sensor + '.yaml'))

    declare_teleop_config = DeclareLaunchArgument(
       'teleop_config', default_value=joy_teleop_path,
       description='Joystick teleop configuration file')

    joy_teleop_node = Node(
       package='joy_teleop',
       executable='joy_teleop',
       parameters=[LaunchConfiguration('teleop_config')],
       remappings=[('cmd_vel', LaunchConfiguration('cmd_vel'))])

    return [declare_teleop_config, joy_teleop_node]


def generate_launch_description():
    pkg_dir = get_package_share_directory('tiago_bringup')

    declare_cmd_vel = DeclareLaunchArgument(
        'cmd_vel', default_value='input_joy/cmd_vel',
        description='Joystick cmd_vel topic')

    joy_node = Node(
        package='joy',
        executable='joy_node',
        name='joystick',
        parameters=[os.path.join(pkg_dir, 'config', 'joy_teleop', 'joy_config.yaml')])

    torso_incrementer_server = Node(
        package='joy_teleop',
        executable='incrementer_server',
        name='incrementer',
        namespace='torso_controller')

    head_incrementer_server = Node(
        package='joy_teleop',
        executable='incrementer_server',
        name='incrementer',
        namespace='head_controller')

    gripper_incrementer_server = Node(
        package='joy_teleop',
        executable='incrementer_server',
        name='incrementer',
        namespace='gripper_controller',
        condition=LaunchConfigurationEquals('end_effector', 'pal-gripper'))

    ld = LaunchDescription()

    # Declare arguments
    # we use OpaqueFunction so the callbacks have access to the context
    ld.add_action(get_robot_name('tiago'))
    ld.add_action(OpaqueFunction(function=declare_args))
    ld.add_action(declare_cmd_vel)

    # Launch joy_teleop_node with the proper config
    ld.add_action(OpaqueFunction(function=launch_setup))
    ld.add_action(joy_node)

    ld.add_action(torso_incrementer_server)
    ld.add_action(head_incrementer_server)
    ld.add_action(gripper_incrementer_server)

    return ld
