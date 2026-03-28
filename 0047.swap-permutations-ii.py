#
# @lc app=leetcode id=47 lang=python3
#
# [47] Permutations II
#

# @lc code=start
class Solution:
    def generate(self, nums: list[int], pos: int) -> set[tuple[int]]:
        if pos == len(nums):
            return {tuple(nums)}

        output = set()
        for i in range(pos, len(nums)):
            nums[pos], nums[i] = nums[i], nums[pos]
            output.update(self.generate(nums, pos + 1))
            nums[pos], nums[i] = nums[i], nums[pos]

        return output

    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        return list(map(list, self.generate(nums, 0)))


# @lc code=end
