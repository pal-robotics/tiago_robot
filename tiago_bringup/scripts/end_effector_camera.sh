#!/bin/bash


# This script by default sets and runs end_effector_camera.launch depending on the vendor:product pair.
# If you want to use two cameras at the same time, you have to plug follow the steps the console outputs

confirmation()
{
        while true; do
            read -p "$*" yn
            case $yn in
                [Yy]* ) break;;
                [Nn]* ) echo "ABORTED"; exit;;
                * ) echo "Please answer Yy/Nn.";;
            esac
        done
}

list_vendor=("1908" "0bda")
list_product=("2311" "5806")
list_frame_rate=(14 30) #frame rate depending on vendor:product

one_camera_automatic() {
    for i in $(seq 0 `expr ${#list_vendor[@]} - 1`);
    do
        echo "searching ${list_vendor[i]}":"${list_product[i]}"
        if [[ $(lsusb | grep ${list_vendor[i]}":"${list_product[i]}) ]]; then

            echo -e "\e[0;32mFound!\e[0m"
            echo "launching libuvc_camera node with following parameters:"
            echo "vendor:=${list_vendor[i]} product:=${list_product[i]} frame_rate:=${list_frame_rate[i]}"

            roslaunch tiago_bringup end_effector_camera.launch vendor:=${list_vendor[i]} product:=${list_product[i]} frame_rate:=${list_frame_rate[i]} &

        fi
    done
}

two_cameras_run() {
    confirmation "Have you plugged only the right usb endoscopic camera?"
    for num_camera in 0 1;
    do
        if [[ $num_camera == 1 ]]; then
            sleep 3
            confirmation "Have you plugged left usb endoscopic camera WITHOUT unplugging the right one?"
        fi
        for i in $(seq 0 `expr ${#list_vendor[@]} - 1`);
        do
            echo "searching ${list_vendor[i]}":"${list_product[i]}"
            if [[ $(lsusb | grep ${list_vendor[i]}":"${list_product[i]}) ]]; then
                echo -e "\e[0;32mFound!\e[0m"
                if [[ $num_camera == 0 ]]; then
                    echo "right" 
                    roslaunch tiago_bringup end_effector_camera.launch vendor:=${list_vendor[i]} product:=${list_product[i]} frame_rate:=${list_frame_rate[i]} camera:="right_camera" index:=${num_camera} &
                elif [[ $num_camera == 1 ]]; then
                    echo "left"
                    roslaunch tiago_bringup end_effector_camera.launch vendor:=${list_vendor[i]} product:=${list_product[i]} frame_rate:=${list_frame_rate[i]} camera:="left_camera" index:=${num_camera} &
                fi
            fi
        done
    done
}

# main

if [[ $1 == "" ]] || [[ $1 == "-h" ]]; then
    echo "Pass the number of cameras you are going to use"
    echo "Example: ./end_effector_camera.sh 1"
elif  [[ $1 == 1 ]]; then
    one_camera_automatic
elif  [[ $1 == 2 ]]; then
    two_cameras_run
else
    echo "Error, you have to pass ./end_effector_camera.sh 1 or ./end_effector_camera.sh 2"
fi

sleep infinity
