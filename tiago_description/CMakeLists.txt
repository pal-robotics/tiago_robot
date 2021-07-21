cmake_minimum_required(VERSION 3.5)
project(tiago_description)

find_package(ament_cmake_auto REQUIRED)


# PAL Robotics stricter build flags, other developers should not worry about this
find_package(ament_cmake_pal QUIET)

ament_auto_find_build_dependencies()


#############
## Testing ##
#############

if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  ament_lint_auto_find_test_dependencies()

  #  find_package(rostest REQUIRED)
    foreach(arm right-arm no-arm) #  left-arm to be implemented
        # Separated to speed up tests, otherwise it's over 13min
        foreach(end_effector no-end-effector pal-gripper pal-hey5 schunk-wsg custom)
            foreach(ft_sensor no-ft-sensor schunk-ft)
              add_launch_test(
                test/test_description.launch.py
                TARGET "tiago_description_${arm}_${end_effector}_${ft_sensor}"
                ARGS "arm:=${arm}" "end_effector:=${end_effector}" "ft_sensor:=${ft_sensor}"
              )
            endforeach()
        endforeach()

        foreach(laser_model no-laser hokuyo sick-551 sick-561 sick-571)
          add_launch_test(
            test/test_description.launch.py
            TARGET "tiago_description_${arm}_${laser_model}"
            ARGS "arm:=${arm}" "laser_model:=${laser_model}"
          )
        endforeach()
        foreach(camera_model no-camera orbbec-astra orbbec-astra-pro asus-xtion)
          add_launch_test(
            test/test_description.launch.py
            TARGET "tiago_description_${arm}_${camera_model}"
            ARGS "arm:=${arm}" "camera_model:=${camera_model}"
          )
        endforeach()
    endforeach()
endif()

# Install Python modules
ament_python_install_package(${PROJECT_NAME})

ament_auto_package(INSTALL_TO_SHARE config gazebo launch Media meshes robots ros2_control urdf)
