#
# @lc app=leetcode id=229 lang=python3
#
# [229] Majority Element II
#

# @lc code=start
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # 1. at most there are two num in the nums with occurence > len(nums) // 3
        # 2. we know how to solve this in O(n) + O(1) to find num whose freq > len(nums) // 2
        # 3. can we divide the problem "two num whose freq > len(nums) // 3" to "num1 whose freq > len(nums) // 2" and "num2 whose freq > len(Nums)"
        # 4. eventually, we double check the find answer num1 and num2 freq to confirm whether there's only one or two satify the condition

        num1 = num2 = None
        vote1 = vote2 = 0
        for num in nums:
            if num1 == num:
                vote1 += 1
            elif num2 == num:
                vote2 += 1
            elif vote1 == 0:
                num1 = num
                vote1 = 1
            elif vote2 == 0:
                num2 = num
                vote2 = 1
            else:
                vote1 -= 1
                vote2 -= 1

        vote1 = nums.count(num1)
        vote2 = nums.count(num2)

        ans = []
        if vote1 > len(nums) // 3:
            ans.append(num1)
        if vote2 > len(nums) // 3:
            ans.append(num2)
        return ans


# @lc code=end
