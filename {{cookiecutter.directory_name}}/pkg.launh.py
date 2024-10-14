from launch import LaunchDescription
from launch_ros.actions import Node

package_name = 'PACKAGE_NAME_HERE'

def generate_launch_description():
    return LaunchDescription([
        Node(
            package=f'{package_name}',
            executable=f'{package_name}_node',
            name=f'{package_name}',
            output='screen'
        ),
    ])
