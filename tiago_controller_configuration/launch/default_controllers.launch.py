# Copyright (c) 2021 PAL Robotics S.L. All rights reserved.
#
#  Redistribution and use in source and binary forms, with or without
#  modification, are permitted provided that the following conditions are met:
#
#  1. Redistributions of source code must retain the above copyright notice,
#  this list of conditions and the following disclaimer.
#  2. Redistributions in binary form must reproduce the above copyright notice,
#  this list of conditions and the following disclaimer in the documentation
#  and/or other materials provided with the distribution.
#  3. Neither the name of the copyright holder nor the names of its
#  contributors may be used to endorse or promote products derived from this
#  software without specific prior written permission.
#
#  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS
#  IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED
#  TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A
#  PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
#  HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
#  SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
#  LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
#  DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
#  THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
#  (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
#  OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

from launch import LaunchDescription
from launch_pal.include_utils import include_launch_py_description
from launch.substitutions import LaunchConfiguration
from launch.actions import DeclareLaunchArgument
from launch.actions import OpaqueFunction
from launch_pal.arg_utils import read_launch_argument
from launch_pal.robot_utils import get_end_effector, get_robot_name


def declare_end_effector(context, *args, **kwargs):

    robot_name = read_launch_argument('robot_name', context)
    print(robot_name)
    return [get_end_effector(robot_name)]


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
        ['launch', 'arm_controller.launch.py'])

    end_effector_controller_launch = include_launch_py_description(
        'tiago_controller_configuration',
        ['launch', LaunchConfiguration('end_effector_controller_launch')])

    ld = LaunchDescription()

    ld.add_action(get_robot_name())
    ld.add_action(OpaqueFunction(function=declare_end_effector))
    ld.add_action(end_effector_controller)

    ld.add_action(mobile_base_controller_launch)
    ld.add_action(joint_state_broadcaster_launch)
    ld.add_action(torso_controller_launch)
    ld.add_action(head_controller_launch)
    ld.add_action(arm_controller_launch)
    ld.add_action(end_effector_controller_launch)

    return ld
