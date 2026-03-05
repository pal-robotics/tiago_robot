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
from launch.actions import DeclareLaunchArgument
from launch_ros.actions import Node
from launch.conditions import LaunchConfigurationNotEquals
from launch_pal.arg_utils import LaunchArgumentsBase
from tiago_description.launch_arguments import TiagoArgs


from dataclasses import dataclass


@dataclass(frozen=True)
class LaunchArguments(LaunchArgumentsBase):

    arm_type: DeclareLaunchArgument = TiagoArgs.arm_type
    end_effector: DeclareLaunchArgument = TiagoArgs.end_effector
    ft_sensor: DeclareLaunchArgument = TiagoArgs.ft_sensor
    base_type: DeclareLaunchArgument = TiagoArgs.base_type


def generate_launch_description():

    # Create the launch description
    ld = LaunchDescription()

    launch_arguments = LaunchArguments()

    launch_arguments.add_to_launch_description(ld)

    declare_actions(ld, launch_arguments)

    return ld


def declare_actions(
    launch_description: LaunchDescription, launch_args: LaunchArguments
):

    from launch_pal import get_pal_configuration
    # PAL helper function to fetch the configuration for this package,
    # which might be installed also from other packages
    joy_teleop_config = get_pal_configuration(
        pkg="joy_teleop",
        node="joy_teleop",
        ld=launch_description)

    joy_teleop_node = Node(
        package='joy_teleop',
        executable='joy_teleop',
        parameters=joy_teleop_config['parameters'],
        remappings=joy_teleop_config['remappings'],)

    launch_description.add_action(joy_teleop_node)

    joy_config = get_pal_configuration(
        pkg="joystick",
        node="joystick",
        ld=launch_description)

    joy_node = Node(
        package='pal_joy',
        executable='game_controller_node',
        name='joystick',
        parameters=joy_config['parameters'])

    launch_description.add_action(joy_node)

    pkg_dir = get_package_share_directory("tiago_bringup")

    joystick_analyzer = Node(
        package='diagnostic_aggregator',
        executable='add_analyzer',
        namespace='joystick',
        output='screen',
        emulate_tty=True,
        parameters=[
            os.path.join(pkg_dir, 'config', 'joy_teleop', 'joystick_analyzers.yaml')
        ],
    )
    launch_description.add_action(joystick_analyzer)

    # starting safe command node for joystick teleop
    safe_command_head = Node(
        package='collision_aware_joint_trajectory_wrapper',
        executable='safe_command_node',
        name='safe_command_node',
        namespace='head_controller',
        output='screen',
        parameters=[{
            'controller_name': 'head_controller'
        }],
        remappings=[
            ('/head_controller/robot_description', '/robot_description'),
            ('/head_controller/robot_description_semantic', '/robot_description_semantic'),
        ]
    )

    launch_description.add_action(safe_command_head)

    safe_command_torso = Node(
        package='collision_aware_joint_trajectory_wrapper',
        executable='safe_command_node',
        name='safe_command_node',
        namespace='torso_controller',
        output='screen',
        parameters=[{
            'controller_name': 'torso_controller'
        }],
        remappings=[
            ('/torso_controller/robot_description', '/robot_description'),
            ('/torso_controller/robot_description_semantic', '/robot_description_semantic'),
        ]
    )

    launch_description.add_action(safe_command_torso)

    torso_incrementer_server = Node(
        package="joy_teleop",
        executable="incrementer_server",
        name="incrementer",
        namespace="torso_controller",
        remappings=[('joint_trajectory', 'safe_command')]
    )

    launch_description.add_action(torso_incrementer_server)

    head_incrementer_server = Node(
        package="joy_teleop",
        executable="incrementer_server",
        name="incrementer",
        namespace="head_controller",
        remappings=[('joint_trajectory', 'safe_command')]
    )

    launch_description.add_action(head_incrementer_server)

    gripper_incrementer_server = Node(
        package="joy_teleop",
        executable="incrementer_server",
        name="incrementer",
        namespace="gripper_controller",
        condition=LaunchConfigurationNotEquals("end_effector", "no-end-effector"),
    )

    launch_description.add_action(gripper_incrementer_server)

    return
