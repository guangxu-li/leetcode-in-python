#
# @lc app=leetcode id=1710 lang=python3
#
# [1710] Maximum Units on a Truck
#

# @lc code=start
import heapq


class Solution:
    def maximumUnits(self, boxTypes: list[list[int]], truckSize: int) -> int:
        boxes = [(-units, i, n) for i, (n, units) in enumerate(boxTypes)]
        heapq.heapify(boxes)
        cnt = 0
        while boxes:
            if truckSize <= 0:
                break

            units, _, n = heapq.heappop(boxes)
            cnt += min(truckSize, n) * -units
            truckSize -= n

        return cnt
# @lc code=end

