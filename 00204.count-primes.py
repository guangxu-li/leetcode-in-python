#
# @lc app=leetcode id=204 lang=python3
#
# [204] Count Primes
#

# @lc code=start
n = 5 * 10**6
isprime = [True] * n
isprime[0] = False
isprime[1] = False

d = 2
while d * d < n:
    if isprime[d]:
        for p in range(d + d, n, d):
            isprime[p] = False
    d += 1

counts = [0] * (5 * 10**6 + 1)
for d in range(3, len(counts)):
    counts[d] += counts[d - 1] + isprime[d - 1]
counts = counts


class Solution:
    def countPrimes(self, n: int) -> int:
        return counts[n]


# @lc code=end
