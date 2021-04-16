#
# @lc app=leetcode id=353 lang=python3
#
# [353] Design Snake Game
#

# @lc code=start
from collections import deque


class SnakeGame:
    dirs = {"U": (-1, 0), "R": (0, 1), "D": (1, 0), "L": (0, -1)}

    def __init__(self, width: int, height: int, food: list[list[int]]):
        """
        Initialize your data structure here.
        @param width - screen width
        @param height - screen height
        @param food - A list of food positions
        E.g food = [[1,1], [1,0]] means the first food is positioned at [1,1], the second is at [1,0].
        """
        self.snake, self.body, self.food = (deque([(0, 0)]), {(0, 0)}, deque(map(tuple, food)))
        self.m, self.n = height, width

    def game_over(self, i: int, j: int) -> bool:
        return i < 0 or i >= self.m or j < 0 or j >= self.n or (i, j) in self.body

    def move(self, direction: str) -> int:
        """
        Moves the snake.
        @param direction - 'U' = Up, 'L' = Left, 'R' = Right, 'D' = Down
        @return The game's score after the move. Return -1 if game over.
        Game over when snake crosses the screen boundary or bites its body.
        """
        i, j, dir = *self.snake[0], self.dirs[direction]
        ni, nj = i + dir[0], j + dir[1]

        if self.food and (ni, nj) == self.food[0]:
            self.snake.appendleft(self.food.popleft())
            self.body.add((ni, nj))
            return len(self.body) - 1

        self.body.remove(self.snake.pop())
        if self.game_over(ni, nj):
            return -1
        self.snake.appendleft((ni, nj))
        self.body.add((ni, nj))

        return len(self.snake) - 1


# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)
# @lc code=end
