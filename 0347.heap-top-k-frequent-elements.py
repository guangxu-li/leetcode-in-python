#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#

# @lc code=start
import heapq
from collections import Counter
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        arr = [(-freq, num) for num, freq in counter.items()]
        heapq.heapify(arr)

        ans = []
        for _ in range(k):
            ans.append(heapq.heappop(arr)[1])
        return ans


# @lc code=end
