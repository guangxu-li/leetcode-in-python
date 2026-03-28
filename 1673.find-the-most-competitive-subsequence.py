#
# @lc app=leetcode id=1673 lang=python3
#
# [1673] Find the Most Competitive Subsequence
#

# @lc code=start
class Solution:
    def mostCompetitive(self, nums: list[int], k: int) -> list[int]:
        output, k = [], len(nums) - k
        for num in nums:
            while output and k and output[-1] > num:
                output.pop()
                k -= 1
            output.append(num)

        return output[: len(output) - k]


# @lc code=end
