#
# @lc app=leetcode id=796 lang=python3
#
# [796] Rotate String
#

# @lc code=start
class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        if len(A) != len(B):
            return False

        arr = [0] * len(B)
        i, j = 0, 1
        while j < len(B):
            if B[i] == B[j]:
                i += 1
                arr[j] = i
                j += 1
            elif i == 0:
                arr[j] = 0
                j += 1
            else:
                i = arr[i - 1]
            
        i, j = 0, 0
        A = A * 2
        while i < len(A) and j < len(B):
            if A[i] == B[j] and j == len(B) - 1:
                return True
            elif A[i] == B[j]:
                i += 1
                j += 1
            else:
                if j:
                    j = arr[j - 1]
                else:
                    i += 1
        return not len(A)
# @lc code=end

