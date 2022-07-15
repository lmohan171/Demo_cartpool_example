import pandas as pd
import time
import gym

#Creating environment
env=gym.make('CartPole-v1')

#4 observations
observation=env.reset()
print(observation)

for _ in range(100):
    env.render()