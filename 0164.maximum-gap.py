#
# @lc app=leetcode id=164 lang=python3
#
# [164] Maximum Gap
#

# @lc code=start
class Solution:
    def maximumGap(self, nums: list[int]) -> int:
        _min, _max, n = min(nums), max(nums), len(nums)
        if _min == _max:
            return 0

        bin_size =  max(1, (_max - _min) // (n - 1))
        bins = [[None, None] for _ in range((_max - _min) // bin_size + 1)]

        for num in nums:
            bin = bins[(num - _min) // bin_size]
            bin[0] = num if bin[0] is None else min(bin[0], num)
            bin[1] = num if bin[1] is None else max(bin[1], num)
        
        bins = [bin for bin in bins if bin[0] is not None]
        return max(b[0] - a[1] for a, b in zip(bins, bins[1:]))

# @lc code=end

