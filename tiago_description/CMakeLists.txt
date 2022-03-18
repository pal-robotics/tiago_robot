cmake_minimum_required(VERSION 2.8.3)
project(tiago_description)

find_package(catkin REQUIRED)

catkin_package()

foreach(dir gazebo Media meshes robots urdf config)
    install(DIRECTORY ${dir}/
        DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/${dir})
endforeach(dir)

#############
## Testing ##
#############

if(CATKIN_ENABLE_TESTING)
  find_package(rostest REQUIRED)
  foreach(arm true false)
      # Separated to speed up tests, otherwise it's over 13min
      foreach(end_effector false pal-gripper pal-hey5 schunk-wsg robotiq-2f-85 robotiq-2f-140 robotiq-epick custom)
          foreach(ft_sensor false schunk-ft)
                      add_rostest(test/test_tiago.test ARGS arm:=${arm}
                          end_effector:=${end_effector} ft_sensor:=${ft_sensor})
          endforeach(ft_sensor)
      endforeach(end_effector)
      foreach(laser_model false hokuyo sick-551 sick-561 sick-571)
                          add_rostest(test/test_tiago.test ARGS arm:=${arm}
                              laser_model:=${laser_model})
      endforeach(laser_model)
      foreach(camera_model false orbbec-astra orbbec-astra-pro asus-xtion)
                          add_rostest(test/test_tiago.test ARGS arm:=${arm}
                              camera_model:=${camera_model})
      endforeach(camera_model)
  endforeach(arm)
endif()
