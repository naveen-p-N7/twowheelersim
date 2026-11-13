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

The `ros2 control` command is provided by the `ros2controlcli` dependency and is useful for checking that the controllers are active.

The launch starts Gazebo, spawns the robot, starts the joint state broadcaster and differential drive controller, and opens RViz.

Drive the robot by publishing `geometry_msgs/msg/Twist` commands:

```bash
ros2 topic pub --rate 10 /diff_cont/cmd_vel_unstamped geometry_msgs/msg/Twist "{linear: {x: 0.2}, angular: {z: 0.0}}"
```

## View the model without Gazebo

```bash
ros2 launch twowheelersim view_model.launch.py
```
