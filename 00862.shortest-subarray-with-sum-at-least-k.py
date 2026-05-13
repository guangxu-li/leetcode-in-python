#
# @lc app=leetcode id=862 lang=python3
#
# [862] Shortest Subarray with Sum at Least K
#

# @lc code=start
import math
from collections import deque


class Solution:
    def shortestSubarray(self, nums: list[int], k: int) -> int:
        # convert to prefix sums and change the problem to find the optimal pair (i, j) to make prefix_sum[j] - prefix_sum[i] >= k
        # monotonic deque
        #   poppush:    increasing order to track "candidate minimums"
        #   query:      find the largest "candidate minimum" that matches the constraint, and (j - i) is one answer candidate
        #   expiration: all candidates minimum that is not larger than the query result is not useful anymore

        n = len(nums)
        prefix_sum = [0] * (n + 1)
        for i in range(1, n + 1):
            prefix_sum[i] = prefix_sum[i - 1] + nums[i - 1]

        ans = math.inf
        mins = deque() # increasing order
        for i in range(n + 1):
            # poppush
            while mins and prefix_sum[mins[-1]] >= prefix_sum[i]:
                mins.pop()
            mins.append(i)

            # query + expiration
            while mins and prefix_sum[i] - prefix_sum[mins[0]] >= k:
                ans = min(ans, i - mins.popleft())

        return ans if math.isfinite(ans) else -1



# @lc code=end
