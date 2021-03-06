#
# @lc app=leetcode id=416 lang=python3
#
# [416] Partition Equal Subset Sum
#

# @lc code=start
# from functools import lru_cache, reduce
# from typing import List, Tuple


class Solution:
    @lru_cache(maxsize=None)
    def partition(self, nums: Tuple[int], pos: int, cur: int) -> bool:
        return not cur or (
            pos != len(nums)
            and cur >= 0
            and (
                self.partition(nums, pos + 1, cur - nums[pos])
                or self.partition(nums, pos + 1, cur)
            )
        )

    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)

        return not s % 2 and self.partition(tuple(nums), 0, s // 2)


# @lc code=end
