import launch
import launch.actions
import launch.substitutions
import launch_ros.actions

def generate_launch_description():
    return launch.LaunchDescription([
        # launch PUB node
        launch_ros.actions.Node(
            package='demo_pkg',  
            executable='node_A.py',
            name='node_A',
            output='screen'
        
        ),
        # launch SUB node
        launch_ros.actions.Node(
            package='demo_pkg',  
            executable='node_B.py',
            name='node_B',
            output='screen'
        ),
    ])