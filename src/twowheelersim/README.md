# Two Wheel Robot Simulation

This package contains a minimal differential drive robot with a box chassis, two powered wheels, and a small support caster. It uses ROS 2 control with Gazebo Harmonic's `gz_ros2_control` plugin.

## Run the simulation

From the workspace root:

```bash
rosdep install --from-paths src --ignore-src -r -y
colcon build --packages-select twowheelersim
source install/setup.bash
ros2 launch twowheelersim launch_sim.launch.py
```

The launch starts Gazebo, spawns the robot, starts the joint state broadcaster and differential drive controller, and opens RViz.

## Drive with keyboard teleop

Keep the simulation running in the first terminal. Open a second terminal, source ROS and the workspace, and install the keyboard teleop package if it is not installed already:

```bash
source /opt/ros/jazzy/setup.bash
source ~/two_wheeler_ws/twowheelersim/install/setup.bash
sudo apt install ros-jazzy-teleop-twist-keyboard
```

Run teleop and remap its `cmd_vel` output to the differential drive controller's command topic:

```bash
ros2 run teleop_twist_keyboard teleop_twist_keyboard --ros-args -r cmd_vel:=/diff_cont/cmd_vel_unstamped
```

Click the terminal running teleop so it receives key presses. Use `i` to move forward, `,` to reverse, `j` and `l` to turn, and `k` to stop. The controller limits forward speed to 0.25 m/s and ramps acceleration for smoother starts.

The `ros2 control` command is provided by the `ros2controlcli` dependency. Check that the controllers are active with:

```bash
ros2 control list_controllers
```

## View the model without Gazebo

```bash
ros2 launch twowheelersim view_model.launch.py
```
