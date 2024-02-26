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
        arm: str = 'no-arm',
        end_effector: str = 'no-ee',
        ft_sensor: str = 'no-ft-sensor'):
    """
    Generate a substitution that creates a text suffix combining the specified tiago arguments.

    The arguments are read as string

    For instance, the suffix for: arm=tiago-arm, end_effector='pal-gripper', ft_sensor='schunk-ft'
    would be '_pal-gripper_schunk-ft'
    """
    if arm in ['no-arm']:
        suffix = arm
        return '_' + suffix

    end_effector = 'no-ee' if end_effector == 'no-end-effector' else end_effector

    components = []
    components.append(end_effector)

    if ft_sensor != 'no-ft-sensor':
        components.append(ft_sensor)

    suffix = '_' + '_'.join(components)
    return suffix
