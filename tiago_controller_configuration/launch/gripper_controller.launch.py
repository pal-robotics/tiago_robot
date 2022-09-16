# Copyright (c) 2022 PAL Robotics S.L.
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
from launch.substitutions import LaunchConfiguration

from launch_ros.actions import Node


# @todo put this somewhere reusable
# @see https://github.com/ros-controls/ros2_control/issues/320
def generate_load_controller_launch_description(
        controller_name, controller_type, pkg_name, controller_params_file):

    pkg_path = get_package_share_directory(pkg_name)
    param_file_path = os.path.join(pkg_path, controller_params_file)

    spawner = Node(package='controller_manager', executable='spawner.py',
                   arguments=[controller_name,
                              '--controller-type', controller_type,
                              '--controller-manager', LaunchConfiguration(
                                  'controller_manager_name'),
                              '--param-file', param_file_path],
                   output='screen')

    return LaunchDescription([
        DeclareLaunchArgument(
            'controller_manager_name', default_value='controller_manager',
            description='Controller manager node name'
        ),
        spawner,
    ])


def generate_launch_description():
    return generate_load_controller_launch_description(
        controller_name='gripper_controller',
        controller_type='joint_trajectory_controller/JointTrajectoryController',
        pkg_name='tiago_controller_configuration',
        controller_params_file=os.path.join(
            'config', 'gripper_controller.yaml'))
