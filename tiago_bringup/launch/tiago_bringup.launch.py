# Copyright (c) 2021 PAL Robotics S.L.
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
from launch_pal.include_utils import include_launch_py_description


def generate_launch_description():
    default_controllers = include_launch_py_description(
        'tiago_controller_configuration',
        ['launch', 'default_controllers.launch.py'])

    twist_mux = include_launch_py_description(
        'tiago_bringup', ['launch', 'twist_mux.launch.py'])

    joystick_teleop = include_launch_py_description(
        'tiago_bringup', ['launch', 'joystick_teleop.launch.py'])

    # @TODO: robot state publisher? already launched in tiago_spawn!
    # @TODO: robot pose publisher
    # @TODO: tf lookup
    # @TODO: dynamic footprint

    return LaunchDescription([
        default_controllers,
        twist_mux,
        joystick_teleop
    ])
