#
# @lc app=leetcode id=378 lang=python3
#
# [378] Kth Smallest Element in a Sorted Matrix
#

# @lc code=start
import heapq


class Solution:
    def kthSmallest(self, matrix: list[list[int]], k: int) -> int:
        def heap() -> int:
            n = len(matrix)
            arr = []
            for i in range(min(k, n)):
                arr.append((matrix[i][0], i, 0))  # (head value of row, head idx, row)
            heapq.heapify(arr)

            num = 0
            for _ in range(k):
                num, i, j = heapq.heappop(arr)
                if j + 1 < n:
                    heapq.heappush(arr, (matrix[i][j + 1], i, j + 1))

            return num

        def binarysearch() -> int:
            n = len(matrix)
            lo, hi = matrix[0][0], matrix[-1][-1]
            while lo < hi:
                mid = (lo + hi) >> 1
                cnt = 0

                row, col = 0, n - 1
                while row < n and col >= 0:
                    val = matrix[row][col]
                    if val <= mid:
                        cnt += col + 1
                        row += 1
                    else:
                        col -= 1

                if cnt < k:
                    lo = mid + 1
                else:
                    hi = mid

            return lo

        # return heap()
        return binarysearch()


# @lc code=end
