#
# @lc app=leetcode id=2672 lang=python3
#
# [2672] Number of Adjacent Elements With the Same Color
#

# @lc code=start
import math
from collections import deque


class Solution:
    def continuousSubarrays(self, nums: list[int]) -> int:
        # expansion: expand right boundary until sliding window max - min > 2
        # correction: shrink left boundary until sliding window max - min <= 2
        # calculation: new subarray cnt = with current value as fixed subarray end, how many starts do we have

        mins = deque()
        maxs = deque()

        cnt = 0
        lo = 0
        for hi, num in enumerate(nums):
            while mins and nums[mins[-1]] >= num:
                mins.pop()
            while maxs and nums[maxs[-1]] <= num:
                maxs.pop()

            mins.append(hi)
            maxs.append(hi)

            while nums[maxs[0]] - nums[mins[0]] > 2:
                if lo == mins[0]:
                    mins.popleft()
                if lo == maxs[0]:
                    maxs.popleft()
                lo += 1

            cnt += hi - lo + 1

        return cnt

    def continuousSubarrays2(self, nums: list[int]) -> int:
        # expansion:    grow window until invalid, then count subarrays of the last valid window.
        # backtrack:    expand backward from the current element to salvage valid previous elements.
        # deduplicate:  subtract the overlapping subarrays to avoid double counting.
        # vs. monotonic deque:
        #   - recalculates min/max on the fly during backward expansion instead of tracking them.
        #   - highly efficient because max diff is 2 (only values [x, x+1, x+2] allowed), bounding the backtrack.
        _min = -math.inf
        _max = math.inf

        cnt = 0
        lo = 0
        for hi, num in enumerate(nums + [math.inf]):
            _max = max(_max, num)
            _min = min(_min, num)

            if _max - _min > 2:
                cnt += (hi - lo) * (hi - lo + 1) // 2

                lo = hi
                _max = _min = num
                while lo > 0 and abs(num - nums[lo - 1]) <= 2:
                    lo -= 1
                    _max = max(_max, nums[lo])
                    _min = min(_min, nums[lo])

                cnt -= (hi - lo) * (hi - lo + 1) // 2

        return cnt
# @lc code=end
