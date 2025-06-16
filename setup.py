from setuptools import setup, find_packages

setup(
    name="panda_mujoco_gym",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "gymnasium>=0.29.1",
        "gymnasium-robotics>=1.2.2",
        "mujoco>=2.3.3",
        "numpy>=1.23.5",
    ],
) 