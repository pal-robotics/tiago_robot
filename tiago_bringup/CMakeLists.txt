cmake_minimum_required(VERSION 2.8.3)
project(tiago_bringup)
find_package(catkin REQUIRED)
catkin_package()

foreach(dir config launch)
    install(DIRECTORY ${dir}/
        DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/${dir})
endforeach(dir)

#install udev rule for end-effector usb camera
install(
    DIRECTORY
        system/
    DESTINATION /
    USE_SOURCE_PERMISSIONS
)
