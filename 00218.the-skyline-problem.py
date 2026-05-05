#
# @lc app=leetcode id=218 lang=python3
#
# [218] The Skyline Problem
#

# @lc code=start
import heapq
from typing import List


class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        # Why sort by the height in descending order for the same l?
        # Think about this case: [[0, 2, 4], [0, 3, 4]]
        points = sorted(p for l, r, h in buildings for p in [(l, -h, r), (r, 0, r)])

        skyline = []
        # max heap (-height, right)
        # It maintains the scanning buildings
        # The initial item represents the horizontal line.
        heights = [(0, float("inf"))]

        for x, y_rev, r in points:
            # x is the x-coordinate of the currently vertical ray
            # y_rev is -height if it's the 'left' point or 0 if it's the 'right' point.
            while x >= heights[0][1]:
                # Remove scanned highest buildings.
                # NOTE: we might not be able to remove all scanned buildings here, but they will be
                # removed in the future.
                # We only need to the heightest building is actually in our view or in progress of scanning.
                heapq.heappop(heights)

            if y_rev:
                # Start to scan a new building
                heapq.heappush(heights, (y_rev, r))

            last_height = skyline[-1][1] if skyline else 0
            max_height = -heights[0][0]
            # If max height is changed, then we found a skyline point.
            if last_height != max_height:
                skyline.append([x, max_height])

        return skyline


# @lc code=end
