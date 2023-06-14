#!/usr/bin/env python
import os
import yaml
import subprocess


def is_motion_file(basepath, motion):
    return os.path.isfile(
        os.path.join(basepath, motion)) and motion.endswith('.yaml')


def main():
    basepath = os.path.expanduser('~/.pal/motions')

    out = subprocess.check_output(["rostopic", "echo",
                                   "/joint_states/name", "-n", "1"])
    current_joints = out.decode("utf-8")
    if os.path.isdir(basepath):
        for motion in os.listdir(basepath):
            if is_motion_file(basepath, motion):
                with open(os.path.join(basepath, motion), 'r') as f:
                    try:
                        motion_param = yaml.load(f, Loader=yaml.FullLoader)
                    except:
                        motion_param = yaml.load(f)
                    for m in motion_param['play_motion']['motions']:
                        m_param = motion_param['play_motion']['motions'][m]
                        motion_ready = True
                        for joint in m_param['joints']:
                            if joint not in current_joints:
                                motion_ready = False
                                break
                        if motion_ready:
                            motion_path = os.path.join(basepath, motion)
                            subprocess.call(["rosparam", "load", "{}"
                                             .format(motion_path)])


if __name__ == "__main__":
    main()
