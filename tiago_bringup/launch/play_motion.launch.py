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
from tiago_description.tiago_launch_utils import get_tiago_hw_arguments


class TiagoXacroConfigSubstitution(Substitution):
    """
    Substitution extracts the tiago hardware args and passes them
    as xacro variables. Used in launch system
    """

    def __init__(self) -> None:
        super().__init__()
        """
        Construct the substitution
        :param: source_file the original YAML file t
        """

    @property
    def name(self) -> List[Substitution]:
        """Getter for name."""
        return "TIAGo Xacro Config"

    def describe(self) -> Text:
        """Return a description of this substitution as a string."""
        return 'Parses tiago hardware launch arguments into xacro \
        arguments potat describe'

    def perform(self, context: LaunchContext) -> Text:
        """
           Generate the robot description and return it as a string
        """

        laser_model = read_launch_argument("laser_model", context)

        arm = read_launch_argument("arm", context)
        end_effector = read_launch_argument("end_effector", context)
        ft_sensor = read_launch_argument("ft_sensor", context)

        return " laser_model:=" + laser_model + \
            " arm:=" + arm + \
            " end_effector:=" + end_effector + \
            " ft_sensor:=" + ft_sensor


def generate_launch_description():
    # @TODO maybe read the description inside the node from the
    # topic instead? It can use it to set the parameter afterwards
    robot_description = {'robot_description': Command(
        [
            ExecutableInPackage(package='xacro', executable="xacro"),
            ' ',
            PathJoinSubstitution(
                [FindPackageShare('tiago_description'),
                 'robots', 'tiago.urdf.xacro']),
            TiagoXacroConfigSubstitution()
        ])
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
                       parameters=[robot_description, approach_planner, motions])

    tiago_args = get_tiago_hw_arguments(
        laser_model=True,
        arm=True,
        end_effector=True,
        ft_sensor=True,
        default_laser_model="sick-571")

    return LaunchDescription([*tiago_args, play_motion])
