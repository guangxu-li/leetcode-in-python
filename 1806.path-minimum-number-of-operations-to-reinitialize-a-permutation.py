#
# @lc app=leetcode id=1806 lang=python3
#
# [1806] Minimum Number of Operations to Reinitialize a Permutation
#

# @lc code=start
class Solution:
    def reinitializePermutation(self, n: int) -> int:
        i, cnt = 1, 0
        while not cnt or i > 1: # i != 1 doesn't work
            i = i * 2 % (n - 1)
            cnt += 1

        return cnt


# @lc code=end

