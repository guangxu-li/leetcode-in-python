#
# @lc app=leetcode id=628 lang=python3
#
# [628] Maximum Product of Three Numbers
#

# @lc code=start
class Solution:
    def maximumProduct(self, nums: list[int]) -> int:
        min1 = min2 = float("inf")
        max1 = max2 = max3 = float("-inf")

        for num in nums:
            if num <= min1:
                min2 = min1
                min1 = num
            elif num <= min2:
                min2 = num
            
            if num >= max1:
                max3 = max2
                max2 = max1
                max1 = num
            elif num >= max2:
                max3 = max2
                max2 = num
            elif num >= max3:
                max3 = num
        
        return max(min1 * min2 * max1, max1 * max2 * max3)


# @lc code=end
