#
# @lc app=leetcode id=735 lang=python3
#
# [735] Asteroid Collision
#

# @lc code=start
from collections import deque


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        dq = deque()
        for e in asteroids:
            if e > 0:
                dq.append(e)
            else:
                e = abs(e)
                while dq and 0 < dq[-1] < e:
                    dq.pop()

                if not dq or dq[-1] < 0:
                    dq.append(-e)
                elif e == dq[-1]:
                    dq.pop()

        return dq


# @lc code=end
