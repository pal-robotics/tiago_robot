#!/bin/bash


# This script by default sets and runs end_effector_camera.launch depending on the vendor:product pair.
# Doesn't work if there are more than one endoscopic cameras at the same time with the same vendor:product. If that's the case you have to do some steps manually.

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

two_cameras_info() {
    right_camera=() #vendor product serial frame_rate
    left_camera=()
    confirmation "Have you plugged only the right usb endoscopic camera?"
    for num_camera in 0 1;
    do
        if [[ $num_camera == 1 ]]; then
            confirmation "Have you unplugged right usb endoscopic camera and plogged the left one?"
        fi
        for i in $(seq 0 `expr ${#list_vendor[@]} - 1`);
        do
            echo "searching ${list_vendor[i]}":"${list_product[i]}"
            if [[ $(lsusb | grep ${list_vendor[i]}":"${list_product[i]}) ]]; then
                echo "wait around 15 seconds to load the information ..."
                lsusb -v | grep -A 14 ${list_vendor[i]}":"${list_product[i]}
                echo "write the found serial number"
                if [[ $num_camera == 0 ]]; then
                    echo "in num_camera=0"
                    read -p "$*" serial_right
                    right_camera=(${list_vendor[i]} ${list_product[i]} ${serial_right} ${list_frame_rate[i]})
                elif [[ $num_camera == 1 ]]; then
                    read -p "$*" serial_left
                    left_camera=(${list_vendor[i]} ${list_product[i]} ${serial_left} ${list_frame_rate[i]})
                fi
            fi
        done
    done
}


two_cameras_run() { 
    confirmation "Have you plugged both cameras?"
    # if 6 args, we fill frame rate for boths cams
    if [[ ${#@} -eq 6 ]]; then
        right_camera=($1 $2 $3)
        left_camera=($4 $5 $6)

        for i in $(seq 0 `expr ${#list_vendor[@]} - 1`);
        do
        if [[ $1 == ${list_vendor[i]} ]] && [[ $2 == ${list_product[i]} ]]; then
            right_camera[3]=${list_frame_rate[i]}
        fi
        if [[ $4 == ${list_vendor[i]} ]] && [[ $5 == ${list_product[i]} ]]; then
            left_camera[3]=${list_frame_rate[i]}
        fi
        done
    fi

   roslaunch tiago_bringup end_effector_camera.launch vendor:=${right_camera[0]} product:=${right_camera[1]} serial:=${right_camera[2]} frame_rate:=${right_camera[3]} &

   roslaunch tiago_bringup end_effector_camera.launch vendor:=${left_camera[0]} product:=${left_camera[1]} serial:=${left_camera[2]} frame_rate:=${left_camera[3]} camera:="left_camera" &
}

# main

if [[ $1 == "" ]] || [[ $1 == "-h" ]]; then
    echo "pass the number of cameras you are going to use"
    echo "Example: ./end_effector_camera.sh 1"
    echo "If you already know the serial numbers of both cameras pass it like this: ./end_effector_camera.sh 2 <vendor_right> <product_right> <serial_right> <vendor_left> <product_left> <serial_left>"
elif  [[ $1 == 1 ]]; then
    one_camera_automatic
elif  [[ $1 == 2 ]]; then
    if [[ ${#@} -lt 7 ]]; then
        two_cameras_info
        two_cameras_run
    else
        two_cameras_run $2 $3 $4 $5 $6 $7
    fi
else
    echo "Error, you have to pass ./end_effector_camera.sh 1 or ./end_effector_camera.sh 2"
fi
        