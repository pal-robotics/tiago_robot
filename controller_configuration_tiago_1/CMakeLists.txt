cmake_minimum_required(VERSION 2.8.3)
project(controller_configuration_tiago_1)

find_package(catkin REQUIRED)

catkin_package()


install(DIRECTORY config
    DESTINATION ${CATKIN_GLOBAL_SHARE_DESTINATION}/tiago_controller_configuration)

