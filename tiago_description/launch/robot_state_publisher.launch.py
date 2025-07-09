# Copyright (c) 2024 PAL Robotics S.L. All rights reserved.
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
from pathlib import Path
import tempfile

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, OpaqueFunction, SetLaunchConfiguration
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
from launch_ros.parameter_descriptions import ParameterValue
from launch_param_builder import load_xacro
from launch_pal.arg_utils import read_launch_argument
from launch_pal.arg_utils import LaunchArgumentsBase
from dataclasses import dataclass
from tiago_description.launch_arguments import TiagoArgs
from launch_pal.robot_arguments import CommonArgs
from launch_pal import calibration_utils


@dataclass(frozen=True)
class LaunchArguments(LaunchArgumentsBase):

    base_type: DeclareLaunchArgument = TiagoArgs.base_type
    arm_type: DeclareLaunchArgument = TiagoArgs.arm_type
    end_effector: DeclareLaunchArgument = TiagoArgs.end_effector
    ft_sensor: DeclareLaunchArgument = TiagoArgs.ft_sensor
    wrist_model: DeclareLaunchArgument = TiagoArgs.wrist_model
    camera_model: DeclareLaunchArgument = TiagoArgs.camera_model
    laser_model: DeclareLaunchArgument = TiagoArgs.laser_model
    has_screen: DeclareLaunchArgument = TiagoArgs.has_screen

    use_sim_time: DeclareLaunchArgument = CommonArgs.use_sim_time
    is_public_sim: DeclareLaunchArgument = CommonArgs.is_public_sim
    namespace: DeclareLaunchArgument = CommonArgs.namespace


def generate_launch_description():

    # Create the launch description and populate
    ld = LaunchDescription()
    launch_arguments = LaunchArguments()

    launch_arguments.add_to_launch_description(ld)

    declare_actions(ld, launch_arguments)

    return ld


def declare_actions(
    launch_description: LaunchDescription, launch_args: LaunchArguments
):
    launch_description.add_action(
        OpaqueFunction(function=create_robot_description_param)
    )

    # Using ParameterValue is needed so ROS knows the parameter type
    # Otherwise https://github.com/ros2/launch_ros/issues/136
    rsp = Node(
        package="robot_state_publisher",
        executable="robot_state_publisher",
        output="both",
        parameters=[
            {
                'use_sim_time': LaunchConfiguration('use_sim_time'),
                "robot_description": ParameterValue(
                    LaunchConfiguration("robot_description"), value_type=str
                ),
            }
        ],
    )

    launch_description.add_action(rsp)

    return


def create_robot_description_param(context, *args, **kwargs):

    xacro_file_path = Path(
        os.path.join(
            get_package_share_directory("tiago_description"),
            "robots",
            "tiago.urdf.xacro",
        )
    )

    xacro_input_args = {
        "arm_type": read_launch_argument("arm_type", context),
        "camera_model": read_launch_argument("camera_model", context),
        "end_effector": read_launch_argument("end_effector", context),
        "ft_sensor": read_launch_argument("ft_sensor", context),
        "laser_model": read_launch_argument("laser_model", context),
        "wrist_model": read_launch_argument("wrist_model", context),
        "base_type": read_launch_argument("base_type", context),
        "has_screen": read_launch_argument("has_screen", context),
        "use_sim_time": read_launch_argument("use_sim_time", context),
        "is_public_sim": read_launch_argument("is_public_sim", context),
        "namespace": read_launch_argument("namespace", context),
    }

    calibration_dir = tempfile.TemporaryDirectory()
    calibration_dir_path = Path(calibration_dir.name)

    input_dir = Path(get_package_share_directory(
        "tiago_description")) / "urdf" / "calibration"

    calibration_xacro_args = calibration_utils.apply_urdf_calibration(
        input_dir, calibration_dir_path)

    xacro_input_args.update(calibration_xacro_args)
    robot_description = load_xacro(xacro_file_path, xacro_input_args)

    return [SetLaunchConfiguration("robot_description", robot_description)]
