import numpy as np
import random

class Pacman:
    def __init__(self):
        self.x = np.array([])
        self.y = np.array([])
        self.myMap = np.array([])
        self.score = 0
        self.done = False

        self.resetCounter = 10  # Max number of attempts to complete $$ cycle of action
        self.actions = {
            "Down": [1, 0],
            "Up": [-1, 0],
            "Right": [0, 1],
            "Left": [0, -1]}

        self.health = 1
        mapSize = 10
        self.map(mapSize, mapSize * 2)  # first map size, second no of wall
        self.ghost(5)  # second entry = no of ghosts
        self.pacman()  # create pacman to a random coordinate
        self.save()

    def save(self):
        self.x, self.y = self.findPacman()

    def reset(self):
        a, b = self.findPacman()  # finds & puts zero to Pacman's current position
        self.myMap[a][b] = 0

        self.myMap[self.x][self.y] = 8  # puts Pacman back to it's original position

        # this for loop is for making 0's to 1, to restore dot's place.
        countx = 0
        for line in self.myMap:
            county = 0
            for element in line:
                if element == 0:
                    self.myMap[countx][county] = 1
                county += 1
            countx += 1

    def restart(self):
        if self.resetCounter != 0:
            self.resetCounter -= 1
            self.step()  # starts to a new random act.

    def create(self, x, no):
        count = 0

        while count != x:
            if no == 8:
                self.myMap[5][5] = no
                count += 1
            else:
                a, b = np.random.randint(9, size=2)
                if self.myMap[a][b] == 1:
                    self.myMap[a][b] = no
                    count += 1

    def findPacman(self):
        # find pacman's coordination
        count = 0
        for x in self.myMap:
            county = 0
            for y in x:
                if y == 8:  # 8 for pacman
                    return count, county
                county += 1
            count += 1
        return

    def map(self, x, y):

        mp = np.ones((x, x))

        self.myMap = np.array(mp)

        # Random walls:
        # return self.create(map, x, 2)  # 2 for walls

        # Map No.1:
        self.myMap[2][3] = 2
        self.myMap[2][4] = 2
        self.myMap[2][4] = 2
        self.myMap[2][4] = 2
        self.myMap[2][4] = 2
        self.myMap[2][4] = 2
        self.myMap[4][4] = 2
        self.myMap[5][4] = 2
        # self.myMap[6][4] = 2
        # self.myMap[7][4] = 2
        self.myMap[6][8] = 2
        self.myMap[7][8] = 2

    def ghost(self, x):

        return self.create(x, 3)  # 3 for ghosts

    def pacman(self):

        return self.create(1, 8)  # 8 for pacman

    def checkBorders(self, x):
        if 0 <= x <= (self.myMap.shape[0] - 1):
            return True
        return False

    def reward(self, x):

        reward = -1  # the simple cost of any movement

        if x == 1:  # checks the position if there is a dot placed on
            reward = 10
        elif x == 3:  # if there is a ghost
            reward = -50
        elif x == 2: # if there is a wall
            reward = -2

        self.score += reward
        return reward

    def step(self, action='random'):
        x, y = self.findPacman()

        rew = 0  # reward

        if self.health > 0:
            self.done = False
            if action == 'random':
                action = random.choice(list(self.actions))  # random choice from the action dictionary

            Coor = self.actions[action]  # gets coordinate from the dict.
            newX = x + Coor[0]  # After action, new coordinates x,y
            newY = y + Coor[1]

            if self.checkBorders(newX) and self.checkBorders(newY):  # checking borders for new X and Y
                rew = self.reward(self.myMap[newX][newY])  # check if there is a dot to collect

                if self.myMap[newX][newY] != 2:  # check if there is a wall or not

                    if self.myMap[newX][newY] == 3:  # check if there is a ghost or not

                        self.health -= 1  # hit ghost

                    else:  # if there is no ghost, then move Pacman to the new coordinate

                        self.myMap[x][y] = 0  # put 0 to the old coordinate

                        self.myMap[newX][newY] = 8  # put 8 to the new coordinate

                        x, y = newX, newY  # new x,y are now our real x, y

        else:
            self.done = True
            self.restart()  # resets the map to the first generated map for new test
        # returns observation, reward, done, info?
        return self.myMap, rew, self.done, self.health

    def render(self):
        print(self.myMap, "\nScore =", self.score, "\nHealth =", self.health, "\n")
