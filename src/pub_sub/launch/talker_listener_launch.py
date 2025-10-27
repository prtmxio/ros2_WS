from launch import LaunchDescription
from launch_ros.actions import Node

TOPIC = 'chatter'

def generate_launch_description(): # this fxn name is fixed
    talker = Node(
        package='pub_sub',
        executable='talker',
        name='talker_node', # can be differnet too,
        # like different for instances of the Talker_node
        parameters=[{
            'topic' : TOPIC
        }]
    )

    listener = Node(
        package='pub_sub',
        executable='listener',
        name='listener_node',
        parameters=[{
            'topic' : TOPIC
        }]
    )

    return LaunchDescription({
        talker, listener
    })