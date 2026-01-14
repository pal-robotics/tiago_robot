# TIAGo Robot - Overview

## Project Overview
The **Tiago Robot** project provides a modular framework for operating the PAL Robotics Tiago robot.  
It includes components for navigation, manipulation, perception, and integration with ROS.  
The project aims to facilitate research, prototyping, and experimentation with robotics applications.

**Core functionalities include:**
- Mobile base navigation with obstacle avoidance
- Manipulation using the robotic arm and gripper
- Sensor integration for perception (RGB-D cameras, LIDAR)
- ROS-based software architecture for modular development

---

## Installation and Setup

### Prerequisites
- Ubuntu 20.04 (or compatible)
- ROS Noetic
- Python 3.8+
- Dependencies listed in `requirements.txt` and ROS packages

### Step-by-Step Setup
1. Clone your forked repository:
    ```bash
    git clone https://github.com/atharv-08svg/tiago_robot.git
    cd tiago_robot
    ```
2. (Optional) Add the original repository as upstream:
    ```bash
    git remote add upstream https://github.com/pal-robotics/tiago_robot.git
    ```
3. Install ROS dependencies:
    ```bash
    rosdep install --from-paths src --ignore-src -r -y
    ```
4. Build the workspace:
    ```bash
    catkin_make
    source devel/setup.bash
    ```

---

## Usage Examples

### Launch the Robot Simulation
```bash
roslaunch tiago_bringup tiago.launch
