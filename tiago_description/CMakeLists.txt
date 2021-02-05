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
  #  foreach(arm true false)
  #      # Separated to speed up tests, otherwise it's over 13min
  #      foreach(end_effector false pal-gripper pal-hey5 schunk-wsg custom)
  #          foreach(ft_sensor false schunk-ft)
  #                      add_rostest(test/test_tiago.test ARGS arm:=${arm}
  #                          end_effector:=${end_effector} ft_sensor:=${ft_sensor})
  #          endforeach(ft_sensor)
  #      endforeach(end_effector)
  #      foreach(laser_model false hokuyo sick-551 sick-561 sick-571)
  #                          add_rostest(test/test_tiago.test ARGS arm:=${arm}
  #                              laser_model:=${laser_model})
  #      endforeach(laser_model)
  #      foreach(camera_model false orbbec-astra orbbec-astra-pro asus-xtion)
  #                          add_rostest(test/test_tiago.test ARGS arm:=${arm}
  #                              camera_model:=${camera_model})
  #      endforeach(camera_model)
  #  endforeach(arm)
endif()

# Install Python modules
# ament_python_install_package(${PROJECT_NAME})

ament_auto_package(INSTALL_TO_SHARE config gazebo Media meshes robots urdf launch)
