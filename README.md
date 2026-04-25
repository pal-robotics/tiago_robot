# TIAGo Robot - Overview

The `tiago_robot` repository contains essential resources for working with PAL Robotics' TIAGo robot, including its URDF files, controllers, and other configurations required for simulation and real-world applications.

## About TIAGo

[TIAGo (Take It and Go)](https://pal-robotics.com/robot/tiago/) is a mobile manipulator robot developed by PAL Robotics. It is widely used in research and industry for a variety of applications, including:

- Mobile manipulation
    
- Human-robot interaction
    
- Assistive robotics
    
- Warehouse automation
    
- AI and reinforcement learning applications
    

## Features of this Repository

This repository includes:

- **URDF/Xacro files**: Detailed robot description models defining TIAGo’s structure and kinematics.
    
- **ROS 2 configuration files**: Launch files, controllers, and sensor integrations for seamless ROS 2-based operation.
    
- **Simulation support**: Compatibility with Gazebo and MoveIt for motion planning and testing.
    
- **Hardware integration**: Configuration files for real-world deployments.
    

## Installation & Setup

### Prerequisites

Ensure that you have the following installed:

- ROS 2 Humble
    
- Gazebo (for simulation support)
    
- MoveIt 2 (for motion planning)
    
- PAL Robotics dependencies
    
- Git (to clone the repository)
    

### Cloning the Repository

```bash
cd ~/tiago_ws/src  # Navigate to your ROS 2 workspace
git clone https://github.com/pal-robotics/tiago_robot.git
cd ~/tiago_ws && colcon build
```

### Setting Up the Environment

Before using the TIAGo robot, source the necessary setup files:

```bash
source ~/tiago_ws/install/setup.bash
```

To avoid sourcing manually every time, add the above line to your `.bashrc` file.

## Repository Structure

### `tiago_bringup`

Contains launch and configuration files required for bringing up the robot in both simulation and real-world environments.

- **`config/`**: Configuration files for various subsystems, including:
    
    - `joy_teleop/`: Configuration for joystick teleoperation.
        
    - `motion_planner/`: Configurations for different end effectors and motion planning setups.
        
    - `motions/`: Predefined motion sequences for different setups.
        
    - `twist_mux/`: Configuration for velocity command multiplexing.
        
- **`launch/`**: Launch files for bringing up different subsystems like joystick teleoperation, motion execution, and twist muxing.
    
- **`module/`**: YAML files specifying configurations for joystick, play motion, and twist mux modules.
    
- **`scripts/`**: Contains `regen_em_file.py`, used for regenerating files from `.em` templates.
    

### `tiago_description`

Contains the URDF, mesh, and configuration files for TIAGo.

- **`config/`**: Contains configuration files like:
    
    - `tiago_configuration.yaml`: General configuration for the robot.
        
    - `tiago.rviz` & `urdf.rviz`: RViz visualization settings.
        
- **`launch/`**: Launch files for visualization and state publishing:
    
    - `robot_state_publisher.launch.py`
        
    - `show.launch.py`
        
- **`meshes/`**: 3D models of the robot components, including:
    
    - `arm/`, `head/`, `sensors/`, `torso/`
        
- **`module/`**: Contains `10_robot_state_publisher.yaml`, which defines robot state publishing settings.
    
- **`robots/`**: Contains `tiago.urdf.xacro`, the main Xacro definition of TIAGo.
    
- **`ros2_control/`**: ROS 2 control configurations, including:
    
    - `gazebo_controller_manager_cfg.yaml`
        
    - `ros2_control.urdf.xacro`
        
    - `transmissions.urdf.xacro`
        
- **`test/`**: Contains test scripts for validating TIAGo’s description:
    
    - `test_description.launch.py`
        
    - `test_xacro.py`
        
- **`tiago_description/`**: Contains Python utilities for launching TIAGo, including:
    
    - `launch_arguments.py`
        
    - `tiago_launch_utils.py`
        
- **`urdf/`**: Contains Xacro files defining specific robot components, structured as:
    
    - `arm/`, `head/`, `sensors/`, `torso/`, `end_effector/`, `calibration/`
        
    - Example: `torso/torso.ros2_control.xacro`, `torso/torso.urdf.xacro`
        

### `tiago_controller_configuration`

Contains configuration files for controlling the robot’s actuators.

- **`config/`**: YAML configurations for various controllers, including:
    
    - `arm_controller.yaml`: Controls the robot's arm.
        
    - `head_controller.yaml`: Controls the head movements.
        
    - `ft_sensor_controller.yaml`: Manages force-torque sensor data.
        
    - `joint_state_broadcaster.yaml`: Handles joint state broadcasting.
        
    - `gravity_compensation_controller_ilm.yaml`: Implements ILM-based gravity compensation.
        
    - `gravity_compensation_controller_parker.yaml`: Implements Parker-based gravity compensation.
        
    - `torso_controller.yaml`: Controls the torso movements.
        
- **`launch/`**: Launch files to initialize controllers, including:
    
    - `default_controllers.launch.py`: Loads and starts default controllers.
        
    - `gravity_compensation_controller.launch.py`: Launches gravity compensation controllers.
        
- **`module/`**: Contains YAML files specifying controller configurations:
    
    - `10_default_controllers.yaml`: Defines default controllers for initialization.
        

### `tiago_robot`

Contains high-level package metadata, including `package.xml` and `CMakeLists.txt`.

## Contributing

We welcome contributions to improve this repository! To contribute:

1. Fork the repository.
    
2. Create a feature branch (`git checkout -b feature-name`).
    
3. Make changes and commit them (`git commit -m "Description of changes"`).
    
4. Push your branch (`git push origin feature-name`).
    
5. Open a pull request on GitHub.
    

## License

This project is licensed under the **Apache 2.0 License** – see the `LICENSE` file for details.
