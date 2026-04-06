#
# @lc app=leetcode id=1929 lang=python3
#
# [1929] Concatenation of Array
#


# @lc code=start
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = [0] * 2 * len(nums)
        for i, num in enumerate(nums):
            ans[i] = ans[i + len(nums)] = num

        return ans


# @lc code=end
