# Copyright 2022 PAL Robotics S.L.
# All Rights Reserved.
#
# Unauthorized copying of this file, via any medium is strictly prohibited,
# unless it was supplied under the terms of a license agreement or
# nondisclosure agreement with PAL Robotics SL. In this case it may not be
# copied or disclosed except in accordance with the terms of that agreement.

import os
from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch_pal.include_utils import include_launch_py_description


def generate_launch_description():
    # Create the launch description and populate
    ld = LaunchDescription([
        include_launch_py_description(
            'robot_control', ['launch', 'robot_control.launch.py'],
            launch_arguments={
              'description_path': os.path.join(
                get_package_share_directory('tiago_description'), 'robots', 'tiago.urdf.xacro'),
              'config_pkg': 'pal_deployer_cfg_tiago',
            }.items(),
        ),
        include_launch_py_description(
            'tiago_bringup', ['launch', 'tiago_bringup.launch.py']
        ),
        include_launch_py_description(
            'tiago_2dnav', ['launch', 'tiago_nav_bringup.launch.py'],
            launch_arguments={
                'use_sim_time': 'False',
                'use_rviz': 'False',
                }.items()),
    ])

    return ld
