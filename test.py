import sys
import time
import gymnasium as gym
import panda_mujoco_gym
from gymnasium.wrappers.pixel_observation import PixelObservationWrapper


if __name__ == "__main__":
    env = gym.make("FrankaPickAndPlaceSparse-v0", render_mode="human")
    env = PixelObservationWrapper(env,
                              pixels_only=False,   # keep the original state
                              pixel_keys=("pixels",),   # default key name
                              )                     # resize/crop kwargs also available

    observation, info = env.reset()


    for _ in range(1000):
        action = env.action_space.sample()
        observation, reward, terminated, truncated, info = env.step(action)

        if terminated or truncated:
            observation, info = env.reset()

        time.sleep(0.2)
        

    env.close()
