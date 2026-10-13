# Installation Guideis

How to set up the tools used in this project. Everything here was tested on **Ubuntu 22.04 with ROS 2 Humble**.

Commands change over time, so for each tool the official documentation is linked first. If a command below fails, follow the official page.

> **Credit:** the robot bring-up software and the lidar driver in section 5 come from [RigBetel Labs](https://github.com/rigbetellabs/tortoisebot). We did not write them.

## Operating system

ROS 2 Humble is designed for **Ubuntu 22.04 LTS (Jammy Jellyfish)**, which is its officially supported platform, so we used it for the whole project. Other Ubuntu versions may need extra work or a different ROS 2 release.

Check your version with:

```bash
lsb_release -a
```

## 1. ROS 2 Humble

Official guide: [ROS 2 Humble installation on Ubuntu](https://docs.ros.org/en/humble/Installation/Ubuntu-Install-Debs.html)

Choose the **desktop** install, which includes RViz2 and the demo nodes. When it finishes, load ROS 2 in every new terminal, or add the line to `~/.bashrc` so it happens automatically:

```bash
source /opt/ros/humble/setup.bash
```

Documentation home: [docs.ros.org/en/humble](https://docs.ros.org/en/humble/index.html)

## 2. RViz2

RViz2 comes with the ROS 2 desktop install. If it's missing:

```bash
sudo apt install ros-humble-rviz2
```

Start it with:

```bash
rviz2
```

Project page: [github.com/ros2/rviz](https://github.com/ros2/rviz)

## 3. Gazebo Ignition (Fortress)

Official guide: [Gazebo Fortress installation on Ubuntu](https://gazebosim.org/docs/fortress/install_ubuntu)

```bash
sudo apt-get update
sudo apt-get install lsb-release wget gnupg
sudo wget https://packages.osrfoundation.org/gazebo.gpg -O /usr/share/keyrings/pkgs-osrf-archive-keyring.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/pkgs-osrf-archive-keyring.gpg] http://packages.osrfoundation.org/gazebo/ubuntu-stable $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/gazebo-stable.list > /dev/null
sudo apt-get update
sudo apt-get install ignition-fortress
```

Check that it works:

```bash
ign gazebo --version
ign gazebo
```

### Connecting Gazebo to ROS 2

These packages let ROS 2 and Gazebo exchange data:

```bash
sudo apt install ros-humble-ros-gz-sim ros-humble-ros-gz-bridge ros-humble-ros-gz-interfaces
```

## 4. OpenCV and image tools

```bash
sudo apt install python3-opencv ros-humble-cv-bridge ros-humble-image-tools
```

| Package | Purpose |
|---|---|
| `python3-opencv` | OpenCV for Python |
| `ros-humble-cv-bridge` | Converts ROS image messages to OpenCV images |
| `ros-humble-image-tools` | Provides the `cam2image` camera node |

Our image-processing steps are explained in [opencv.md](opencv.md).

## 5. TortoiseBot software (RigBetel Labs)

The robot bring-up and lidar driver come from RigBetel Labs' repository. Their instructions are in the [TortoiseBot README](https://github.com/rigbetellabs/tortoisebot) (use the `ros2-humble` branch). In short, on the laptop:

```bash
mkdir -p ~/tb_ws/src && cd ~/tb_ws/src
git clone -b ros2-humble https://github.com/rigbetellabs/tortoisebot.git
cd ~/tb_ws
rosdep install --from-paths src --ignore-src -r -y
colcon build --packages-ignore ydlidar_sdk ydlidar_ros2_driver v4l2_camera tortoisebot_firmware tortoisebot_imu
source install/setup.bash
```

The hardware-only packages are built separately on the robot itself. Follow their README for that, and for connecting the robot to your Wi-Fi.

> **Note:** their setup has you enter your Wi-Fi name and password in a file on the SD card. Keep that file out of any repository.

## 6. Check that everything works

```bash
ros2 --help
rviz2
ign gazebo
python3 -c "import cv2; print(cv2.__version__)"
```

If all four run without errors, the setup is complete.
