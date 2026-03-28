#
# @lc app=leetcode id=1806 lang=python3
#
# [1806] Minimum Number of Operations to Reinitialize a Permutation
#

# @lc code=start
class Solution:
    def reinitializePermutation(self, n: int) -> int:
        init, arr, cnt = list(range(n)), list(range(n)), 0

        while not cnt or arr != init:
            arr = [arr[n // 2 + (i - 1) // 2] if i % 2 else arr[i // 2] for i in range(n)]
            cnt += 1

        return cnt


# @lc code=end
