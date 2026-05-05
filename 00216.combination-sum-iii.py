#
# @lc app=leetcode id=216 lang=python3
#
# [216] Combination Sum III
#

# @lc code=start
class Solution:
    def comb(self, i: int, k: int, n: int) -> list[list[int]]:
        if not n and not k:
            return [[]]
        if not k or n <= 0:
            return []
        
        output = [] 
        for j in range(i, 10):
            for nxt in self.comb(j + 1, k - 1, n - j):
                output.append([j] + nxt)
            
        return output

    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        return self.comb(1, k, n)
# @lc code=end

