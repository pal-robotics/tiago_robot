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
        controller_name='joint_state_controller',
        controller_type='joint_state_controller/JointStateController',
        pkg_name='tiago_controller_configuration',
        controller_params_file=os.path.join(
            'config', 'joint_state_controller.yaml'))
