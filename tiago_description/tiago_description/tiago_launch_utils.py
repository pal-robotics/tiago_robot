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


def get_tiago_hw_suffix(
        arm=None,
        wrist_model=None,
        end_effector=None,
        ft_sensor=None,
        camera_model=None):
    """
    Generate a substitution that creates a text suffix combining the specified tiago arguments.

    The arguments are read as string

    For instance, the suffix for: arm=right-arm, wrist_model=wrist-2017, end_effector='pal-gripper'
    would be 'right-arm_wrist-2017_pal-gripper'
    """
    suffix = ''

    if arm is not None:
        suffix += arm
        suffix += '_'
    if wrist_model is not None:
        suffix += wrist_model
        suffix += '_'
    if end_effector is not None:
        suffix += end_effector
        suffix += '_'
    if ft_sensor is not None:
        suffix += ft_sensor
        suffix += '_'
    if camera_model is not None:
        suffix += camera_model
        suffix += '_'
    suffix = suffix[:-1]  # remove last _
    return suffix
