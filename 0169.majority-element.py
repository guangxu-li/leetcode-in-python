#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#


# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate, vote = 0, 0
        for num in nums:
            if vote == 0:
                candidate = num
            if candidate == num:
                vote += 1
            else:
                vote -= 1
        return candidate


# @lc code=end
