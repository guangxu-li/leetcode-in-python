#
# @lc app=leetcode id=3918 lang=python3
#
# [3918] Sum of Primes Between Number and Its Reverse
#

# @lc code=start
from bisect import bisect_left, bisect_right
from itertools import islice

n = 1000
isprime = [True] * (n + 1)
isprime[0] = False
isprime[1] = False

d = 2
while d * d <= n:
    if isprime[d]:
        for m in range(d + d, n + 1, d):
            isprime[m] = False
    d += 1

primes = [d for d in range(n + 1) if isprime[d]]


class Solution:
    def sumOfPrimesInRange(self, n: int) -> int:
        def reverse(num: int) -> int:
            rev = 0
            while num:
                rev = rev * 10 + num % 10
                num //= 10
            return rev

        num, rev = n, reverse(n)
        lo = bisect_left(primes, min(num, rev))
        hi = bisect_right(primes, max(num, rev))
        return sum(islice(primes, lo, hi))


# @lc code=end
