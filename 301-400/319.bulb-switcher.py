#
# @lc app=leetcode id=319 lang=python3
#
# [319] Bulb Switcher
#

# @lc code=start
import math


# Let's make the round number and bulb index number start from 1.
# After n rounds,
#   - i-th bulb is off if number i has even number of distinct factors, since it's toggled event number times
#   - i-th bulb is odd if number i has odd number of distinct factors, since it's toggled odd number times
#
# To make a number has odd number of distinct factors, it must be a perfect square.
#   - Assume we have a number n
#   - m is a factor of n
#   - then n/m is also a factor of n
# So only when m = n = sqrt(n), we can make the number of factors odd.
#
# Now the question becomes, how many perfect square we can have that is <= n
# The answer is apparently sqrt(n), which is the answer of this problem.
class Solution:
    def bulbSwitch(self, n: int) -> int:
        return math.isqrt(n)
