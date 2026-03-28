#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#

# @lc code=start
class Solution:
    def generate(self, nums: list[int], pos: int) -> list[list[int]]:
        if pos == len(nums):
            return [nums.copy()]

        output = []
        for i in range(pos, len(nums)):
            nums[pos], nums[i] = nums[i], nums[pos]
            output.extend(self.generate(nums[:], pos + 1))
            nums[pos], nums[i] = nums[i], nums[pos]
        
        return output

    def permute(self, nums: list[int]) -> list[list[int]]:
        return self.generate(nums, 0)
# @lc code=end

