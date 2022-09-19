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

from launch.substitutions import PythonExpression, LaunchConfiguration


def get_tiago_hw_suffix(
        arm=False,
        wrist_model=False,
        end_effector=False,
        ft_sensor=False,
        camera_model=False,
        **kwargs):
    """
    Generate a substitution that creates a text suffix combining the specified tiago arguments

    The arguments are read as LaunchConfigurations

    For instance, the suffix for: arm=right-arm, wrist_model=wrist-2017, end_effector="pal-gripper"
    would be "right-arm_wrist-2017_pal-gripper"
    """

    suffix_elements = ["'"]
    if arm:
        suffix_elements.append(LaunchConfiguration("arm"))
        suffix_elements.append("_")
    if wrist_model:
        suffix_elements.append(LaunchConfiguration("wrist_model"))
        suffix_elements.append("_")
    if end_effector:
        suffix_elements.append(LaunchConfiguration("end_effector"))
        suffix_elements.append("_")
    if ft_sensor:
        suffix_elements.append(LaunchConfiguration("ft_sensor"))
        suffix_elements.append("_")
    if camera_model:
        suffix_elements.append(LaunchConfiguration("camera_model"))
        suffix_elements.append("_")
    suffix_elements = suffix_elements[:-1]  # remove last _
    suffix_elements.append("'")
    print(suffix_elements)
    return PythonExpression(suffix_elements)
