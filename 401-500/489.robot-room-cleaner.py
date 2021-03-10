#
# @lc app=leetcode id=489 lang=python3
#
# [489] Robot Room Cleaner
#

# @lc code=start
# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
#class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

class Solution:
    dirs = ((-1, 0), (0, 1), (1, 0), (0, -1))

    def __init__(self):
        self.visited = set()

    def restore(self):
        self.robot.turnRight()
        self.robot.turnRight()
        self.robot.move()
        self.robot.turnRight()
        self.robot.turnRight()

    def explore(self, pos: tuple = (0, 0), d: int = 0) -> None:
        self.robot.clean()
        self.visited.add(pos)

        for i in range(4):
            nxt = (pos[0] + self.dirs[d][0], pos[1] + self.dirs[d][1])
            if nxt not in self.visited and self.robot.move():
                self.explore(nxt, d)
                self.restore()
            d = (d + 1) % 4

            self.robot.turnRight()

    def cleanRoom(self, robot) -> None:
        """
        :type robot: Robot
        :rtype: None
        """
        self.robot = robot
        self.explore()
        
# @lc code=end

