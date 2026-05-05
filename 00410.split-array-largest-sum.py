#
# @lc app=leetcode id=410 lang=python3
#
# [410] Split Array Largest Sum
#


# @lc code=start
class Solution:
    def splitArray(self, nums: list[int], k: int) -> int:
        # n = len(nums)
        # answer space: [max(nums), sum(nums)] without the constrain k
        #   - smallest: split into n subarrays
        #   - largest: split into 1 subarray
        # The more we split, the smaller answer we have
        # binary search the answer:
        #   1. based on the candidate answer, we can calculate the corresponding minimum number of splits
        #   2. if min_split < k: valid answer, but we wanna try if there's even smaller answer can fit in this condition
        #   3. if min_split = k: valid answer, but we wanna try if there's even smaller answer can fit in this condition
        #   4. if min_split > k: we need the answer to be higher

        # min splits to make sure every non-empty subarrays sum is not larger than threshold
        def min_split(threshold: int) -> int:
            cnt = 1  # the whole array as a split
            _sum = 0
            for num in nums:
                if _sum + num > threshold:
                    _sum = 0
                    cnt += 1
                _sum += num

            return cnt

        lo, hi = max(nums), sum(nums)
        while lo <= hi:
            mid = (lo + hi) // 2
            c = min_split(mid)

            if c <= k:
                hi = mid - 1
            else:
                lo = mid + 1

        return lo


# @lc code=end
