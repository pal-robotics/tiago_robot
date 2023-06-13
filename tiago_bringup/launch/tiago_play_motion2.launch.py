# Copyright (c) 2023 PAL Robotics S.L. All rights reserved.
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
from launch.actions import OpaqueFunction

from launch_pal.arg_utils import read_launch_argument
from launch_pal.include_utils import include_launch_py_description
from launch_pal.robot_utils import (get_arm,
                                    get_end_effector,
                                    get_ft_sensor,
                                    get_robot_name)

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

    motions_file = 'tiago_motions' + get_tiago_hw_suffix(arm=arm,
                                                         end_effector=end_effector,
                                                         ft_sensor=ft_sensor) + '.yaml'

    play_motion2_config = os.path.join(
        get_package_share_directory('tiago_bringup'), 'config', 'motions', motions_file)

    play_motion2 = include_launch_py_description(
        'play_motion2', ['launch', 'play_motion2.launch.py'],
        launch_arguments={'play_motion2_config': play_motion2_config}.items())

    return [play_motion2]


def generate_launch_description():

    ld = LaunchDescription()

    # Declare arguments
    # we use OpaqueFunction so the callbacks have access to the context
    ld.add_action(get_robot_name('tiago'))
    ld.add_action(OpaqueFunction(function=declare_args))

    # Launch play_motion2 with the proper config
    ld.add_action(OpaqueFunction(function=launch_setup))

    return ld
