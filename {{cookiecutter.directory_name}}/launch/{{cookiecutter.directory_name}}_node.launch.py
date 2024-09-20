from launch import LaunchDescription
from launch_ros.actions import Node
import os

package_name = os.path.basename(os.path.dirname(os.path.dirname(__file__)))

def generate_launch_description():
    return LaunchDescription([
        Node(
            package=f'{package_name}',
            executable=f'{package_name}_node',
            name=f'{package_name}',
            output='screen'
        ),
    ])
