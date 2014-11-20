cmake_minimum_required(VERSION 2.8.3)
project(tiago_description)

find_package(catkin REQUIRED)

catkin_package()

foreach(dir gazebo Media meshes robots urdf)
    install(DIRECTORY ${dir}/
        DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/${dir})
endforeach(dir)
