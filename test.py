import Pacman, time

env = Pacman()
env.reset()

for x in range(1, 10):
    env.render()
    state, reward, isDone, health = env.step("random")
    # env.step(action)
    # all actions: up, down, left, right

    time.sleep(1)

    if isDone:
        print('ended')
        break