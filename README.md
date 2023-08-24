# 10x10 Pacman Environment for Reinforcement Learning

This repository contains a simple Pacman game environment designed in Python, specifically designed for Reinforcement Learning (RL) purposes. The environment provides a foundational platform for experimenting with RL algorithms and gaining insights into their behavior within the context of the Pacman game. The project was developed as part of an AI homework assignment in 2018.

## Environment Description

The Pacman environment is represented on a 10x10 grid, where different elements are denoted by specific values:

- `8`: Pacman
- `1`: Food (10 points)
- `2`: Wall (-2 points)
- `3`: Ghost (-50 points)
- `0`: Visited/Empty (-1 point)

The primary objective is to guide Pacman through the environment, collecting food while evading ghosts and obstacles. The game features a scoring system that rewards points for collecting food and penalizes points for encountering ghosts or colliding with walls.

![pacman](https://user-images.githubusercontent.com/55997117/154800815-df61af74-b9d6-4d01-a9d7-fe9ae65a2e42.gif)

## Pacman.py

The `pacman.py` file implements the `Pacman` class, which plays a central role in the Pacman environment. It includes various functionalities such as movement mechanics, scoring computation, collision detection, health management, and dynamic map generation. This file serves as the core foundation for creating and interacting with the Pacman game environment.

## Test.py

The `test.py` file demonstrates how to utilize the `Pacman` class for simulating Pacman's actions and interactions within the game environment. This script simulates Pacman's actions randomly, without any specific algorithm guiding its decisions. It is primarily used to test the environment and observe how Pacman moves, collects food, and responds to various challenges.
