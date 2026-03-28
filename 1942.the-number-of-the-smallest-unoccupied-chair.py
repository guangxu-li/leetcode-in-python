#
# @lc app=leetcode id=1942 lang=python3
#
# [1942] The Number of the Smallest Unoccupied Chair
#

# @lc code=start
from heapq import heappop, heappush


class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        target = times[targetFriend][0]
        chairs = list(range(len(times)))

        occupied = []
        for start, end in sorted(times):
            while occupied and occupied[0][0] <= start:
                _, chair = heappop(occupied)
                heappush(chairs, chair)

            chair = heappop(chairs)
            if target == start:
                return chair

            heappush(occupied, (end, chair))


# @lc code=end
