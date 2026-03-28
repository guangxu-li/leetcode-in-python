#
# @lc app=leetcode id=480 lang=python3
#
# [480] Sliding Window Median
#

# @lc code=start
import heapq


class Solution:
    def clean_heap(self, heap: list, set: set) -> None:
        while heap and heap[0][1] not in set:
            heapq.heappop(heap)

    def move_to(
        self,
        out_heap: list[tuple],
        out_set: set[int],
        in_heap: list[tuple],
        in_set: set[int],
    ) -> None:
        val, i = heapq.heappop(out_heap)
        heapq.heappush(in_heap, (-val, i))
        out_set.remove(i)
        in_set.add(i)

    def medianSlidingWindow(self, nums: list[int], k: int) -> list[float]:
        medians, min_heap, max_heap, min_set, max_set = [], [], [], set(), set()
        for i, num in enumerate(nums):
            # remove outcome num
            min_set.discard(i - k)
            max_set.discard(i - k)
            self.clean_heap(min_heap, min_set)
            self.clean_heap(max_heap, max_set)

            # pop valid tuple from min_heap
            heapq.heappush(min_heap, (num, i))
            min_set.add(i)
            self.move_to(min_heap, min_set, max_heap, max_set)

            # rebalance two heap if necesscary
            while len(max_set) - len(min_set) > 1:
                self.move_to(max_heap, max_set, min_heap, min_set)

            if i >= k - 1:
                self.clean_heap(min_heap, min_set)
                self.clean_heap(max_heap, max_set)
                medians.append(
                    -max_heap[0][0] if k % 2 else (min_heap[0][0] - max_heap[0][0]) / 2
                )

        return medians


# @lc code=end
