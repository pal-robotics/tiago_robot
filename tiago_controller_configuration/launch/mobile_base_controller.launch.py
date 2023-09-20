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

from ament_index_python.packages import get_package_share_directory

from controller_manager.launch_utils import generate_load_controller_launch_description
from launch_pal.param_utils import merge_param_files


def generate_launch_description():

    default_config = os.path.join(
        get_package_share_directory('tiago_controller_configuration'),
        'config', 'mobile_base_controller.yaml')

    calibration_config = '/etc/calibration/master_calibration.yaml'

    if os.path.exists(calibration_config):
        params_file = merge_param_files([default_config, calibration_config])
    else:
        params_file = default_config

    return generate_load_controller_launch_description(
        controller_name='mobile_base_controller',
        controller_type='diff_drive_controller/DiffDriveController',
        controller_params_file=params_file)
