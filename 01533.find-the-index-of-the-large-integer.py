#
# @lc app=leetcode id=1533 lang=python3
#
# [1533] Find the Index of the Large Integer
#

# Constraints:
# 2 <= arr.length <= 5 * 105
# 1 <= arr[i] <= 100
# All elements of arr are equal except for one element which is larger than all other elements.

# @lc code=start
# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
# class ArrayReader(object):
# 	 # Compares the sum of arr[l..r] with the sum of arr[x..y]
# 	 # return 1 if sum(arr[l..r]) > sum(arr[x..y])
# 	 # return 0 if sum(arr[l..r]) == sum(arr[x..y])
# 	 # return -1 if sum(arr[l..r]) < sum(arr[x..y])
#    def compareSub(self, l: int, r: int, x: int, y: int) -> int:
#
# 	 # Returns the length of the array
#    def length(self) -> int:
#


class Solution:
    def getIndex(self, reader: "ArrayReader") -> int:
        lo, hi = 0, reader.length() - 1
        while lo < hi:
            # i = (lo + hi) >> 1
            #
            # lo + hi is odd -> (lo + hi) // 2 == (lo + hi - 1) // 2:
            #   left: lo, i
            #   right: i + 1, hi
            # lo + hi is even -> (lo + hi) // 2 - 1 == (lo + hi - 1) // 2:
            #   left: lo, i - 1
            #   right: i + 1, hi

            r = (lo + hi - 1) >> 1
            a = ((lo + hi) >> 1) + 1

            print(lo, r, a, hi)
            m = reader.compareSub(lo, r, a, hi)

            if m == 0:
                return r + 1
            elif m == 1:  # left > right
                hi = r
            else:  # left < right
                lo = a

        return lo


# @lc code=end
