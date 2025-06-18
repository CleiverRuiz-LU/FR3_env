from setuptools import setup, find_packages

setup(
    name="panda-mujoco-gym",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "mujoco==2.3.3",
        "gymnasium==0.29.1", 
        "gymnasium-robotics==1.2.2",
        "stable-baselines3==2.2.1"
    ],
) 