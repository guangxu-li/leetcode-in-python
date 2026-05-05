#
# @lc app=leetcode id=1482 lang=python3
#
# [1482] Minimum Number of Days to Make m Bouquets
#


# @lc code=start
class Solution:
    def minDays(self, bloomDay: list[int], m: int, k: int) -> int:
        lo, hi = min(bloomDay), max(bloomDay) + 1
        while lo < hi:
            mid = (lo + hi) >> 1

            bouquets = 0
            flowers = 0
            for day in bloomDay:
                if day <= mid:
                    flowers += 1
                else:
                    flowers = 0

                if flowers == k:
                    bouquets += 1
                    flowers = 0

            if bouquets < m:
                lo = mid + 1
            else:
                hi = mid

        return lo if lo <= max(bloomDay) else -1


# @lc code=end
