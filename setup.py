from distutils.core import setup

setup(
    name='pyvirtual',
    packages=['pyvirtual'],
    version='0.1',
    license='MIT',
    description='Python Computer Vision and Robotics Simulator',
    author='Computer Vision Zone',
    author_email='contact@computervision.zone',
    url='https://github.com/infocvzone/pyvirtual',
    keywords=['ComputerVision', 'Simulator', 'Robotics', 'Drone'],
    install_requires=[
        'pyzmq',
        'opencv-python',
    ],
    python_requires='>=3.7',  # Requires any version >= 3.7

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: MIT License',
        'Programming Language :: Python :: 3',
    ],
)
