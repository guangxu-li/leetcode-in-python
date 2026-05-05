#
# @lc app=leetcode id=698 lang=python3
#
# [698] Partition to K Equal Sum Subsets
#

# @lc code=start
class Solution:
    def solvable(self, nums: tuple[int], groups: list[int], pos: int) -> bool:
        if pos == len(nums):
            return True

        for i in range(len(groups)):
            if groups[i] >= nums[pos]:
                groups[i] -= nums[pos]
                if self.solvable(nums, groups, pos + 1):
                    return True
                groups[i] += nums[pos]

        return False

    def canPartitionKSubsets(self, nums: list[int], k: int) -> bool:
        target, rem = divmod(sum(nums), k)

        return not rem and self.solvable(tuple(sorted(nums, reverse=True)), [target] * k, 0)


# @lc code=end
