from launch import LaunchDescription
from launch.actions import RegisterEventHandler, TimerAction
from launch.event_handlers import OnProcessExit
from launch_ros.actions import Node


def generate_launch_description():
    spawn_model = Node(
        package='ros_gz_sim',
        executable='create',
        name='spawn_twowheelersim',
        arguments=[
            '-topic', 'robot_description',
            '-name', 'twowheelersim',
            '-z', '0.05',
        ],
        output='screen',
    )

    joint_state_broadcaster = Node(
        package='controller_manager',
        executable='spawner',
        name='joint_state_broadcaster_spawner',
        arguments=[
            'joint_state_broadcaster',
            '--controller-manager', '/controller_manager',
            '--controller-manager-timeout', '60',
        ],
        output='screen',
    )

    diff_drive_controller = Node(
        package='controller_manager',
        executable='spawner',
        name='diff_drive_controller_spawner',
        arguments=[
            'diff_cont',
            '--controller-manager', '/controller_manager',
            '--controller-manager-timeout', '60',
        ],
        output='screen',
    )

    load_controllers = RegisterEventHandler(
        OnProcessExit(
            target_action=spawn_model,
            on_exit=[TimerAction(
                period=3.0,
                actions=[joint_state_broadcaster, diff_drive_controller],
            )],
        )
    )

    return LaunchDescription([spawn_model, load_controllers])
