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
      foreach(end_effector false pal-gripper pal-hey5 schunk-wsg)
          foreach(ft_sensor false schunk-ft)
              foreach(laser_model false hokuyo sick-551 sick-561 sick-571)
                  add_rostest(test/test_tiago.test ARGS arm:=${arm}
                      end_effector:=${end_effector} ft_sensor:=${ft_sensor}
                      laser_model:=${laser_model})
              endforeach(laser_model)
          endforeach(ft_sensor)
      endforeach(end_effector)
  endforeach(arm)
endif()
