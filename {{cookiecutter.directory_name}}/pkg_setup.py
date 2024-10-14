from setuptools import setup
from glob import glob

package_name = 'PACKAGE_NAME_HERE'

setup(
    name=package_name,
    version='1.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            [f'resource/{package_name}']),
        (f'share/{package_name}', ['package.xml']),
        (f'share/{package_name}', glob('launch/*.launch.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='root',
    maintainer_email='bmtrungvp@gmail.com',
    description=f'{package_name} Package',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            f'{package_name}_node = {package_name}.{package_name}:main'
        ],
    },
)
