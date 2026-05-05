#
# @lc app=leetcode id=556 lang=python3
#
# [556] Next Greater Element III
#

# @lc code=start
import bisect


class Solution:
    def nextGreaterElement(self, n: int) -> int:
        num = list(str(n))
        i = len(num) - 2
        while i >= 0 and num[i] >= num[i + 1]:
            i -= 1
        if i == -1:
            return -1
        
        rem = num[:i:-1]
        num = num[:i + 1]
        j = bisect.bisect(rem, num[i])
        if rem[j] == num[i]:
            j += 1
        num[i], rem[j] = rem[j], num[i]

        higher = int("".join(num) + "".join(rem))
        return higher if higher <= (1 << 31) - 1 else -1

# @lc code=end

