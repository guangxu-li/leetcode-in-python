#
# @lc app=leetcode id=287 lang=python3
#
# [287] Find the Duplicate Number
#

# @lc code=start
from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        def cyclesort1(nums: List[int]) -> int:
            i = num = 0
            while num != nums[i]:
                num, nums[i] = nums[i], num
                i = num

            return num

        def cyclesort2(nums: List[int]) -> int:
            n = len(nums)
            i = 0
            while i < n:
                j = nums[i] - 1
                if nums[i] != nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]
                else:
                    i += 1
            for i in range(n):
                if nums[i] != i + 1:
                    return nums[i]

        def binarysearch(nums: List[int]) -> int:
            # [1, 2, 2, 3, 4]
            lo, hi = 0, len(nums)
            while lo < hi:
                mid = (lo + hi) // 2
                cnt = sum(num <= mid for num in nums)
                if cnt > mid:
                    hi = mid
                else:
                    lo = mid + 1
            return lo

        def bitcount(nums: List[int]) -> int:
            duplicate = 0
            m = len(nums)
            n = m - 1
            for bit in range(n.bit_length()):
                mask = 1 << bit
                cnt = 0
                for i in range(m):
                    cnt += (nums[i] & mask) > 0  # actual
                    cnt -= (i & mask) > 0  # perfect

                # If duplicate value d appears k times:
                #   - extra copies of d contribute (k - 1) copies of this bit
                #   - missing values remove at most (k - 2) copies of this bit
                #
                # actual array:     [1, 2, 3, 3, 3, 3, 6, 7] | len=m        | k = 4
                # "perfect" array:  [1, 2, 3, 4, 5, 6, 7]    | len=m - 1
                #
                # it equals to compare the bit set count between:
                # duplicate = [3, 3, 3] # k - 1
                # missing = [4, 5]      # k - 2
                #
                # if the duplicate has the bit, the extra copies contribute at least one more 1 than the missing side can remove
                # if the duplicate does not have the bit, the extra copied contributes 0, so cnt cannot be positive.
                if cnt > 0:
                    duplicate |= mask
            return duplicate

        def cycledetection(nums: List[int]) -> int:
            tortoise = nums[0]
            hare = nums[nums[0]]
            while tortoise != hare:
                tortoise = nums[tortoise]
                hare = nums[nums[hare]]

            tortoise = 0
            while tortoise != hare:
                tortoise = nums[tortoise]
                hare = nums[hare]

            return hare

        # return cyclesort1(nums)
        # return cyclesort2(nums)
        # return binarysearch(nums)
        # return bitcount(nums)
        return cycledetection(nums)


# @lc code=end
