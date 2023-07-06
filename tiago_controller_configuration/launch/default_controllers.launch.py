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

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, OpaqueFunction
from launch.conditions import LaunchConfigurationNotEquals
from launch.substitutions import LaunchConfiguration
from launch_pal.arg_utils import read_launch_argument
from launch_pal.include_utils import include_launch_py_description
from launch_pal.robot_utils import get_arm, get_end_effector, get_robot_name


def declare_robot_args(context, *args, **kwargs):

    robot_name = read_launch_argument('robot_name', context)

    return [get_arm(robot_name),
            get_end_effector(robot_name)]


def launch_end_effector_controller(context, *args, **kwargs):

    if (read_launch_argument('end_effector', context) == 'no-end-effector'):
        return []

    end_effector_launcher = read_launch_argument('end_effector_controller_launch', context)
    end_effector_controller_launch = include_launch_py_description(
        'tiago_controller_configuration',
        ['launch', end_effector_launcher],
        condition=LaunchConfigurationNotEquals('arm', 'no-arm'))

    return [end_effector_controller_launch]


def generate_launch_description():

    end_effector_controller = DeclareLaunchArgument(
        'end_effector_controller_launch',
        default_value=[LaunchConfiguration('end_effector'), '_controller.launch.py'],
        description='end effector controller launch file')

    mobile_base_controller_launch = include_launch_py_description(
        'tiago_controller_configuration',
        ['launch', 'mobile_base_controller.launch.py'])

    joint_state_broadcaster_launch = include_launch_py_description(
        'tiago_controller_configuration',
        ['launch', 'joint_state_broadcaster.launch.py'])

    torso_controller_launch = include_launch_py_description(
        'tiago_controller_configuration',
        ['launch', 'torso_controller.launch.py'])

    head_controller_launch = include_launch_py_description(
        'tiago_controller_configuration',
        ['launch', 'head_controller.launch.py'])

    arm_controller_launch = include_launch_py_description(
        'tiago_controller_configuration',
        ['launch', 'arm_controller.launch.py'],
        condition=LaunchConfigurationNotEquals('arm', 'no-arm'))

    ld = LaunchDescription()

    ld.add_action(get_robot_name('tiago'))
    ld.add_action(OpaqueFunction(function=declare_robot_args))
    ld.add_action(end_effector_controller)

    ld.add_action(mobile_base_controller_launch)
    ld.add_action(joint_state_broadcaster_launch)
    ld.add_action(torso_controller_launch)
    ld.add_action(head_controller_launch)
    ld.add_action(arm_controller_launch)
    ld.add_action(OpaqueFunction(function=launch_end_effector_controller))

    return ld
