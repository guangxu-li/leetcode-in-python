#
# @lc app=leetcode id=386 lang=python3
#
# [386] Lexicographical Numbers
#

# @lc code=start
class Solution:
    def lexicalOrder(self, n: int) -> list[int]:
        ret = [1]
        for _ in range(n - 1):
            i = ret[-1] * 10
            while i > n:
                i //= 10
                i += 1

                while not i % 10:
                    i //= 10
            ret.append(i)
        
        return ret
# @lc code=end
