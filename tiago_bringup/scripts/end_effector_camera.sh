#!/bin/bash

# This script sets and runs end_effector_camera.launch depending on the vendor:product pair.
# Doesn't work if there are more than one endoscopic cameras at the same time with the same vendor:product. If that's the case you have to follow the manual.

list_vendor=("1908" "0bda") #vendor
list_product=("2311" "5806")
list_frame_rate=(14 30) #frame rate depending on vendor:product
for i in $(seq 0 `expr ${#list_vendor[@]} - 1`);
do
    echo "searching ${list_vendor[i]}":"${list_product[i]}"
    if [[ $(lsusb | grep ${list_vendor[i]}":"${list_product[i]}) ]]; then

        echo -e "\e[0;32mFound!\e[0m"
        echo "launching libuvc_camera node with following parameters:"
        echo "vendor:=${list_vendor[i]} product:=${list_product[i]} frame_rate:=${list_frame_rate[i]}"

        roslaunch tiago_bringup end_effector_camera.launch vendor:=${list_vendor[i]} product:=${list_product[i]} frame_rate:=${list_frame_rate[i]} #and run launch file passing args

    fi
done