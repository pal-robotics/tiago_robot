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

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_pal.substitutions import LoadFile
from launch_ros.actions import Node
from tiago_description.tiago_launch_utils import (generate_robot_description_action,
                                                  get_tiago_hw_arguments, get_tiago_hw_suffix)


def generate_launch_description():
    tiago_hw_suffix = get_tiago_hw_suffix(
        arm=True, wrist_model=False, end_effector=True, ft_sensor=True)

    robot_description = {
        'robot_description': generate_robot_description_action()
    }

    robot_description_semantic_config = LoadFile(
        [get_package_share_directory('tiago_moveit_config'),
         '/config/srdf/tiago_', tiago_hw_suffix, '.srdf']
    )
    robot_description_semantic = {
        'robot_description_semantic': robot_description_semantic_config
    }

    approach_planner = [get_package_share_directory('tiago_bringup'),
                        '/config/approach_planner/approach_planner_',
                        tiago_hw_suffix, '.yaml']

    motions = [get_package_share_directory('tiago_bringup'),
               '/config/motions/tiago_motions_', tiago_hw_suffix, '.yaml']

    play_motion = Node(package='play_motion',
                       executable='play_motion',
                       output='both',
                       parameters=[
                           robot_description,
                           robot_description_semantic,
                           approach_planner,
                           motions,
                       ])

    # TIAGo description arguments
    tiago_args = get_tiago_hw_arguments(
        laser_model=True,
        arm=True,
        end_effector=True,
        ft_sensor=True,
        camera_model=True)

    return LaunchDescription([*tiago_args, play_motion])
