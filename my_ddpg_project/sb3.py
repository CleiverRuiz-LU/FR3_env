import gymnasium as gym
from panda_mujoco_gym.envs.pick_and_place import FrankaPickAndPlaceEnv

from stable_baselines3 import SAC
env = gym.make("FrankaPickAndPlaceDense-v0", render_mode="rgb_array")

model = SAC("MultiInputPolicy", env, verbose=1)
model.learn(total_timesteps=100000, log_interval=4)
model.save("sac_PAP")

del model

model = SAC.load("sac_PAP")

obs, info = env.reset()
while True:
    action, _states = model.predict(obs, deterministic=True)
    obs, reward, terminated, truncated, info = env.step(action)
    if terminated or truncated:
        obs, info = env.reset()