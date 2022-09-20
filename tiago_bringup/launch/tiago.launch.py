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
from launch_pal.include_utils import include_launch_py_description


def generate_launch_description():
    # Create the launch description and populate
    robot_control_launch = include_launch_py_description(
        'robot_control', ['launch', 'robot_control.launch.py'],
        launch_arguments={
          'description_path': os.path.join(
            get_package_share_directory('tiago_description'), 'robots', 'tiago.urdf.xacro'),
          'config_pkg': 'pal_deployer_cfg_tiago',
        }.items(),
    )

    tiago_bringup_launch = include_launch_py_description(
        'tiago_bringup', ['launch', 'tiago_bringup.launch.py']
    )

    tiago_nav_bringup_launch = include_launch_py_description(
        'tiago_2dnav', ['launch', 'tiago_nav_bringup.launch.py'],
        launch_arguments={
            'use_sim_time': 'False',
            'use_rviz': 'False',
          }.items())

    ld = LaunchDescription()

    ld.add_action(robot_control_launch)
    ld.add_action(tiago_bringup_launch)
    ld.add_action(tiago_nav_bringup_launch)

    return ld
