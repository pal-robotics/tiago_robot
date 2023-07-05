cmake_minimum_required(VERSION 3.5)
project(tiago_bringup)

find_package(ament_cmake_auto REQUIRED)
ament_auto_find_build_dependencies()

if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  ament_lint_auto_find_test_dependencies()
endif()

install(PROGRAMS scripts/regen_em_file.py
  DESTINATION lib/${PROJECT_NAME}
)

# @TODO
# install(PROGRAMS scripts/end_effector_camera.sh
#   DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
# )

ament_auto_package(INSTALL_TO_SHARE config launch)

