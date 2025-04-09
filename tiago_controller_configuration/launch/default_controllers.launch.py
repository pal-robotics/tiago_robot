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
from dataclasses import dataclass
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import GroupAction, OpaqueFunction
from launch_pal.arg_utils import read_launch_argument
from controller_manager.launch_utils import generate_load_controller_launch_description
from launch_pal.arg_utils import LaunchArgumentsBase
from launch.actions import DeclareLaunchArgument
from launch_pal.include_utils import include_scoped_launch_py_description
from launch.substitutions import PythonExpression, LaunchConfiguration
from launch_pal.robot_arguments import CommonArgs
from tiago_description.launch_arguments import TiagoArgs
from launch.conditions import (
    LaunchConfigurationNotEquals,
    IfCondition,
    UnlessCondition
)


@dataclass(frozen=True)
class LaunchArguments(LaunchArgumentsBase):

    base_type: DeclareLaunchArgument = TiagoArgs.base_type
    arm_type: DeclareLaunchArgument = TiagoArgs.arm_type
    arm_motor_model: DeclareLaunchArgument = TiagoArgs.arm_motor_model
    end_effector: DeclareLaunchArgument = TiagoArgs.end_effector
    ft_sensor: DeclareLaunchArgument = TiagoArgs.ft_sensor
    is_public_sim: DeclareLaunchArgument = CommonArgs.is_public_sim
    use_sim_time: DeclareLaunchArgument = CommonArgs.use_sim_time


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
    # Create the extra configs from the LAs
    pkg_share_folder = get_package_share_directory(
        "tiago_controller_configuration")

    launch_description.add_action(
        OpaqueFunction(function=launch_mobile_base_controller))

    joint_state_broadcaster = GroupAction(
        [
            generate_load_controller_launch_description(
                controller_name="joint_state_broadcaster",
                controller_params_file=os.path.join(
                    pkg_share_folder, "config", "joint_state_broadcaster.yaml"
                ),
            )
        ],
    )
    launch_description.add_action(joint_state_broadcaster)

    # Torso controller
    torso_controller = GroupAction(
        [
            generate_load_controller_launch_description(
                controller_name="torso_controller",
                controller_params_file=os.path.join(
                    pkg_share_folder, "config", "torso_controller.yaml"
                ),
            )
        ],
    )

    launch_description.add_action(torso_controller)

    # Head controller
    head_controller = GroupAction(
        [
            generate_load_controller_launch_description(
                controller_name="head_controller",
                controller_params_file=os.path.join(
                    pkg_share_folder, "config", "head_controller.yaml"
                ),
            )
        ],
        forwarding=False,
    )

    launch_description.add_action(head_controller)

    # Arm controller
    arm_controller = GroupAction(
        [
            generate_load_controller_launch_description(
                controller_name='arm_controller',
                controller_params_file=os.path.join(
                    pkg_share_folder, 'config', 'arm_controller.yaml'))
        ],
        forwarding=False,
        condition=LaunchConfigurationNotEquals("arm_type", "no-arm"),
    )

    launch_description.add_action(arm_controller)

    # Gravity compensation controller
    gravity_compensation_controller = include_scoped_launch_py_description(
        pkg_name="tiago_controller_configuration",
        paths=["launch", "gravity_compensation_controller.launch.py"],
        launch_arguments={"arm_motor_model": launch_args.arm_motor_model},
        condition=UnlessCondition(PythonExpression(
                [
                    "'",
                    LaunchConfiguration("is_public_sim"),
                    "' == 'True' or '",
                    LaunchConfiguration("arm_type"),
                    "' == 'no-arm'",
                ]
            )
        ),
    )

    launch_description.add_action(gravity_compensation_controller)

    # FT Sensor
    ft_sensor_controller = GroupAction(
        [
            generate_load_controller_launch_description(
                controller_name="ft_sensor_controller",
                controller_params_file=os.path.join(
                    pkg_share_folder, "config", "ft_sensor_controller.yaml"
                ),
            )
        ],
        forwarding=False,
        condition=IfCondition(
            PythonExpression(
                [
                    "'",
                    LaunchConfiguration("arm_type"),
                    "' != 'no-arm' and '",
                    LaunchConfiguration("ft_sensor"),
                    "' != 'no-ft-sensor'",
                ]
            )
        ),
    )

    launch_description.add_action(ft_sensor_controller)

    # Configure LA dependant controllers
    launch_description.add_action(OpaqueFunction(
        function=configure_end_effector))

    return


def launch_mobile_base_controller(context, *args, **kwargs):

    base_type = read_launch_argument("base_type", context)
    use_sim_time = read_launch_argument("use_sim_time", context)
    is_public_sim = read_launch_argument("is_public_sim", context)

    base_controller_package = base_type + "_controller_configuration"

    mobile_base_controller = include_scoped_launch_py_description(
        pkg_name=base_controller_package,
        paths=["launch", "mobile_base_controller.launch.py"],
        launch_arguments={
            "use_sim_time": use_sim_time,
            "is_public_sim": is_public_sim,
        }
    )

    return [mobile_base_controller]


def configure_end_effector(context, *args, **kwargs):

    end_effector = read_launch_argument("end_effector", context)
    end_effector_underscore = end_effector.replace('-', '_')

    if (end_effector == 'no-end-effector'):
        return []

    if "robotiq" in end_effector:
        ee_pkg_name = "pal_robotiq_controller_configuration"
        ee_launch_file = "robotiq_gripper_controller.launch.py"
    else:
        ee_pkg_name = f"{end_effector_underscore}_controller_configuration"
        ee_launch_file = f"{end_effector_underscore}_controller.launch.py"

    end_effector_controller = include_scoped_launch_py_description(
        pkg_name=ee_pkg_name,
        paths=['launch', ee_launch_file],
        condition=IfCondition(
            PythonExpression(
                [
                    "'",
                    LaunchConfiguration("arm_type"),
                    "' != 'no-arm'",
                ]
            )
        ),
    )

    return [end_effector_controller]
