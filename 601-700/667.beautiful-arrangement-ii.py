#
# @lc app=leetcode id=667 lang=python3
#
# [667] Beautiful Arrangement II
#

# @lc code=start
class Solution:
    def constructArray(self, n: int, k: int) -> list[int]:
        """
        When k == n - 1 -> [1, n, 2, n - 1, 3, n - 2, ...]

        If k != n - 1 -> [1, 2, 3, ..., n - k - 1] as prefix (n - k - 1) elements and 1 distance
        The number of unused number is k + 1, and we wanna used these constructArray(k + 1, k)
        which should be [n - k, n, n - k + 1, n - 1]
        """
        return list(range(1, n - k)) + [
            n - i // 2 if i % 2 else n - k + i // 2 for i in range(k + 1)
        ]


# @lc code=end
