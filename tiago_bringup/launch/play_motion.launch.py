import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription, Substitution
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare, ExecutableInPackage
from launch.substitutions import Command, PathJoinSubstitution
from launch import Substitution, SomeSubstitutionsType, LaunchContext
from typing import List
from typing import Text
from launch_pal.arg_utils import read_launch_argument
from launch_pal.substitutions import LoadFile
from tiago_description.tiago_launch_utils import get_tiago_hw_arguments, get_tiago_hw_suffix, generate_robot_description_action


def generate_launch_description():
    robot_description = {
        "robot_description": generate_robot_description_action()
    }

    robot_description_semantic_config = LoadFile(
        [get_package_share_directory("tiago_moveit_config"), "/config/srdf/tiago_",
         get_tiago_hw_suffix(arm=True, wrist_model=False,
                             end_effector=True, ft_sensor=True), ".srdf"]
    )
    robot_description_semantic = {
        "robot_description_semantic": robot_description_semantic_config
    }

    # @TODO use the tiago args to correctly load the proper file
    approach_planner = os.path.join(
        get_package_share_directory('tiago_bringup'),
        'config/approach_planner', 'approach_planner_pal-gripper.yaml'
    )

    # @TODO use the tiago args to correctly load the proper file
    motions = os.path.join(
        get_package_share_directory('tiago_bringup'),
        'config/motions', 'tiago_motions_pal-gripper.yaml'
    )

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
