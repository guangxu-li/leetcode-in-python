#
# @lc app=leetcode id=1509 lang=python3
#
# [1509] Minimum Difference Between Largest and Smallest Value in Three Moves
#

# @lc code=start
class Solution:
    def minDifference(self, nums: list[int]) -> int:
        """
        https://leetcode.com/problems/minimum-difference-between-largest-and-smallest-value-in-three-moves/discuss/730567/JavaC%2B%2BPython-Straight-Forward
        
        4 plans:
            1. kill 3 biggest -> ret: A[-4] - A[0]
            2. kill 2 biggest and 1 smallest -> ret: A[-3] - A[1]
            3. kill 1 biggest and 2 smallest -> ret: A[-2] - A[2]
            4. kill 3 smallest -> ret: A[-1] - A[3]
        """
        
        nums.sort() # could optimized by using quick sort
        return min(a - b for a, b in zip(nums[-4:], nums[:4]))
        
# @lc code=end
