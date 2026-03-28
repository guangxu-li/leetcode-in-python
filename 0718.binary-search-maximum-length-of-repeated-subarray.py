#
# @lc app=leetcode id=718 lang=python3
#
# [718] Maximum Length of Repeated Subarray
#

# @lc code=start
class Solution:
    def findLength(self, A: list[int], B: list[int]) -> int:
        def found(n: int) -> bool:
            sub_a = {A[i : i + n] for i in range(len(A) - n + 1)}
            return any(B[i : i + n] in sub_a for i in range(len(B) - n + 1))

        A, B = "".join(map(chr, A)), "".join(map(chr, B))
        lo, hi = 0, min(len(A), len(B))
        while lo <= hi:
            mid = (lo + hi) >> 1
            if found(mid):
                lo = mid + 1
            else:
                hi = mid - 1

        return hi


# @lc code=end
