#
# @lc app=leetcode id=912 lang=python3
#
# [912] Sort an Array
#


# @lc code=start
import math
from collections import Counter
from random import randint
from typing import List


class Solution:
    def merge_sort(self, nums: List[int]) -> List[int]:
        def merge(nums: List[int], i: int, mid: int, j: int):
            tmp = []
            l, r = i, mid + 1
            while l <= mid or r <= j:
                num1 = nums[l] if l <= mid else math.inf
                num2 = nums[r] if r <= j else math.inf
                if num1 <= num2:
                    l += 1
                    tmp.append(num1)
                else:
                    r += 1
                    tmp.append(num2)
            nums[i : j + 1] = tmp

        def merge_sort_recursive(nums: List[int], i: int, j: int) -> List[int]:
            if i >= j:
                return

            # split
            mid = (i + j) >> 1
            merge_sort_recursive(nums, i, mid)
            merge_sort_recursive(nums, mid + 1, j)
            merge(nums, i, mid, j)

        def merge_sort_iterative_1(nums: List[int]):
            stack = [(0, len(nums) - 1, False)]
            while stack:
                (i, j, ready) = stack.pop()
                if i >= j:
                    continue

                mid = (i + j) >> 1
                if ready:
                    merge(nums, i, mid, j)
                    continue

                stack.append((i, j, True))
                stack.append((i, mid, False))
                stack.append((mid + 1, j, False))

        def merge_sort_iterative_2(nums: List[int]):
            n, size = len(nums), 1
            while size < n:
                for i in range(0, n, size * 2):
                    mid = min(i + size - 1, n - 1)
                    j = min(i + size * 2 - 1, n - 1)
                    merge(nums, i, mid, j)
                size *= 2

        # merge_sort_iterative_1(nums)
        merge_sort_iterative_2(nums)
        # merge_sort_recursive(nums, 0, len(nums) - 1)
        return nums

    def count_sort(self, nums: List[int]) -> List[int]:
        counter = Counter(nums)
        _min, _max = min(nums), max(nums)
        ans = []
        for num in range(_min, _max + 1):
            while counter[num]:
                counter[num] -= 1
                ans.append(num)
        return ans

    def radix_sort(self, nums: List[int]) -> List[int]:
        _min, _max = min(nums), max(nums)

        mask = 1
        while (_max - _min) >= mask:
            buckets = [[] for _ in range(10)]
            for num in nums:
                digit = (num - _min) // mask % 10
                buckets[digit].append(num)

            i = 0
            for bucket in buckets:
                for num in bucket:
                    nums[i] = num
                    i += 1
            mask *= 10

        return nums

    def quick_sort(self, nums: List[int]) -> List[int]:
        def quick_partition(nums: List[int], i: int, j: int) -> int:
            p = randint(i, j)
            nums[j], nums[p] = nums[p], nums[j]

            for k in range(i, j):
                if nums[k] < nums[j]:
                    nums[i], nums[k] = nums[k], nums[i]
                    i += 1
            nums[i], nums[j] = nums[j], nums[i]
            return i

        def quick_sort_recursive(nums: List[int], i: int, j: int):
            if i >= j:
                return

            p = quick_partition(nums, i, j)
            quick_sort_recursive(nums, i, p - 1)
            quick_sort_recursive(nums, p + 1, j)

        def quick_sort_iterative(nums: List[int]):
            stack = [(0, len(nums) - 1)]
            while stack:
                (i, j) = stack.pop()
                if i >= j:
                    continue

                p = quick_partition(nums, i, j)
                stack.append((i, p - 1))
                stack.append((p + 1, j))

        quick_sort_iterative(nums)
        # quick_sort_recursive(nums, 0, len(nums) - 1)
        return nums

    def heap_sort(self, nums: List[int]) -> List[int]:
        def heapify(nums: List[int], n: int, i: int) -> List[int]:
            while i < n:
                l, r, j = i * 2 + 1, i * 2 + 2, i
                if l < n and nums[j] < nums[l]:
                    j = l
                if r < n and nums[j] < nums[r]:
                    j = r

                if i == j:
                    break
                nums[i], nums[j] = nums[j], nums[i]
                i = j

        n = len(nums)
        for i in reversed(range(n // 2)):
            heapify(nums, n, i)

        for i in reversed(range(n)):
            nums[0], nums[i] = nums[i], nums[0]
            heapify(nums, i, 0)

        return nums

    def sortArray(self, nums: List[int]) -> List[int]:
        return self.merge_sort(nums)
        # return self.count_sort(nums)
        # return self.radix_sort(nums)
        # return self.quick_sort(nums)
        # return self.heap_sort(nums)


# @lc code=end
