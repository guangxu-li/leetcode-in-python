#
# @lc app=leetcode id=1481 lang=python3
#
# [1481] Least Number of Unique Integers after K Removals
#

# @lc code=start
from collections import Counter
import heapq


class Solution:
    def findLeastNumOfUniqueInts(self, arr: list[int], k: int) -> int:
        freq_heap = [(cnt, num) for num, cnt in Counter(arr).items()]
        heapq.heapify(freq_heap)
        
        while k > 0:
            cnt, _ = heapq.heappop(freq_heap)
            k -= cnt
        return len(freq_heap) + (k < 0)
# @lc code=end

