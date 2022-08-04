#!/bin/bash


# This script by default sets and runs end_effector_camera.launch depending on the vendor:product pair.
# If you want to use two cameras at the same time you have to open a second terminal and do rosrun tiago_bringup end_effector_camera.sh left_camera

# each column is one camera and its configuration
list_vendor=("1908" "0bda" "1902" "1902")
list_product=("2311" "5806" "8301" "0327")
# You can detect the compatible frame rate using the command `v4l2-ctl --list-formats-ext`
list_frame_rate=(14 30 30 30) #frame rate depending on vendor:product

cameras_run()
{
local camera=${1:-"camera"}
local video_device=${2:-0}
local rotation=${3:-0}
local framerate=""
for i in $(seq 0 `expr ${#list_vendor[@]} - 1`);
do
    echo "searching ${list_vendor[i]}":"${list_product[i]}"
    if [[ $(lsusb | grep ${list_vendor[i]}":"${list_product[i]}) ]]; then
        echo -e "\e[0;32mFound!\e[0m" 
        framerate=${list_frame_rate[i]} 
    fi
done
if [[ -z "$framerate" ]]; then
    echo -e "\033[0;33mUnable to determine the framerate from vendor ID, trying with default framerate of 30Hz\e[0m"
    framerate="30"
fi
roslaunch tiago_bringup end_effector_camera.launch framerate:=${list_frame_rate[i]} camera:=${camera} rotation:=${rotation} video_device:=${video_device}
}

# main

case $1 in
    "-h")
        echo "Pass nothing or right_camera or left_camera"
        echo "Example: rosrun tiago_bringup end_effector_camera.sh right_camera"
    ;;
    "" | "camera")
        cameras_run "camera" /dev/video0 $2
    ;;
    "right_camera")
        cameras_run $1 /dev/video0 $2
    ;;
    "left_camera")
        cameras_run $1 /dev/video2 $2
    ;;
    # unccoment the following to add the posibility to add an extra camera
    # "x_camera")
    #     confirmation "Have you plugged left usb endoscopic camera WITHOUT unplugging the right one?"
    #     cameras_run $1 2
    # ;;
    *)
        echo "Pass nothing or right_camera or left_camera"
        echo "Example: rosrun tiago_bringup end_effector_camera.sh right_camera"
    ;;
esac
