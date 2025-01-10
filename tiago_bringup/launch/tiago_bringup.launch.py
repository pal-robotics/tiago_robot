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
from launch.actions import DeclareLaunchArgument

from launch_pal.include_utils import include_scoped_launch_py_description
from launch_pal.arg_utils import LaunchArgumentsBase
from launch_pal.robot_arguments import CommonArgs
from tiago_description.launch_arguments import TiagoArgs

from dataclasses import dataclass


@dataclass(frozen=True)
class LaunchArguments(LaunchArgumentsBase):

    base_type: DeclareLaunchArgument = TiagoArgs.base_type
    arm_type: DeclareLaunchArgument = TiagoArgs.arm_type
    arm_motor_model: DeclareLaunchArgument = TiagoArgs.arm_motor_model
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

    # Create the launch description
    ld = LaunchDescription()

    launch_arguments = LaunchArguments()

    launch_arguments.add_to_launch_description(ld)

    declare_actions(ld, launch_arguments)

    return ld


def declare_actions(
    launch_description: LaunchDescription, launch_args: LaunchArguments
):

    default_controllers = include_scoped_launch_py_description(
        pkg_name="tiago_controller_configuration",
        paths=["launch", "default_controllers.launch.py"],
        launch_arguments={
            "arm_type": launch_args.arm_type,
            "arm_motor_model": launch_args.arm_motor_model,
            "end_effector": launch_args.end_effector,
            "ft_sensor": launch_args.ft_sensor,
            "base_type": launch_args.base_type,
            "use_sim_time": launch_args.use_sim_time,
            "is_public_sim": launch_args.is_public_sim,
        },
    )

    launch_description.add_action(default_controllers)

    play_motion2 = include_scoped_launch_py_description(
        pkg_name="tiago_bringup",
        paths=["launch", "tiago_play_motion2.launch.py"],
        launch_arguments={
            "arm_type": launch_args.arm_type,
            "end_effector": launch_args.end_effector,
            "ft_sensor": launch_args.ft_sensor,
            "use_sim_time": launch_args.use_sim_time,
        },
    )

    launch_description.add_action(play_motion2)

    twist_mux = include_scoped_launch_py_description(
        pkg_name="tiago_bringup",
        paths=["launch", "twist_mux.launch.py"],
        launch_arguments={
            "base_type": launch_args.base_type,
            "use_sim_time": launch_args.use_sim_time,
        }
    )

    launch_description.add_action(twist_mux)

    robot_state_publisher = include_scoped_launch_py_description(
        pkg_name="tiago_description",
        paths=["launch", "robot_state_publisher.launch.py"],
        launch_arguments={
            "arm_type": launch_args.arm_type,
            "end_effector": launch_args.end_effector,
            "ft_sensor": launch_args.ft_sensor,
            "wrist_model": launch_args.wrist_model,
            "laser_model": launch_args.laser_model,
            "camera_model": launch_args.camera_model,
            "base_type": launch_args.base_type,
            "has_screen": launch_args.has_screen,
            "namespace": launch_args.namespace,
            "use_sim_time": launch_args.use_sim_time,
            "is_public_sim": launch_args.is_public_sim,
        },
    )

    launch_description.add_action(robot_state_publisher)

    return
