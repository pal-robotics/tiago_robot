cmake_minimum_required(VERSION 2.8.3)
project(tiago_bringup)
find_package(catkin REQUIRED)
catkin_package()


install(PROGRAMS scripts/end_effector_camera.sh
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)

foreach(dir config launch)
    install(DIRECTORY ${dir}/
        DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/${dir})
endforeach(dir)
