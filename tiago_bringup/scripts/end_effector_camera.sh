#!/bin/bash


# This script by default sets and runs end_effector_camera.launch depending on the vendor:product pair.
# If you want to use two cameras at the same time you have to open a second terminal and do rosrun tiago_bringup end_effector_camera.sh left_camera

# each column is one camera and its configuration
list_vendor=("1908" "0bda")
list_product=("2311" "5806")
list_frame_rate=(14 30) #frame rate depending on vendor:product

cameras_run() {
camera=${1:-"camera"}
index=${2:-0}
for i in $(seq 0 `expr ${#list_vendor[@]} - 1`);
do
    echo "searching ${list_vendor[i]}":"${list_product[i]}"
    if [[ $(lsusb | grep ${list_vendor[i]}":"${list_product[i]}) ]]; then
        echo -e "\e[0;32mFound!\e[0m" 
        roslaunch tiago_bringup end_effector_camera.launch vendor:=${list_vendor[i]} product:=${list_product[i]} frame_rate:=${list_frame_rate[i]} camera:=${camera} index:=${index}
    fi
done
}

# main

case $1 in
    "-h")
        echo "Pass nothing or right_camera or left_camera"
        echo "Example: rosrun tiago_bringup end_effector_camera.sh right_camera"
    ;;
    "" | "camera")
        cameras_run "camera" 0
    ;;
    "right_camera")
        cameras_run $1 0
    ;;
    "left_camera")
        cameras_run $1 1
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
