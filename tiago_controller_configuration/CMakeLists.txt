cmake_minimum_required(VERSION 3.8)
project(tiago_controller_configuration)

find_package(ament_cmake_auto REQUIRED)
ament_auto_find_build_dependencies()

if(pal_module_cmake_FOUND)
  pal_register_modules(
    module/20_default_controllers.yaml
  )
endif()

if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  ament_lint_auto_find_test_dependencies()
endif()

ament_auto_package(INSTALL_TO_SHARE config launch)
