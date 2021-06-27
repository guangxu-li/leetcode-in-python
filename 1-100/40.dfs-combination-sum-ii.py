#
# @lc app=leetcode id=40 lang=python3
#
# [40] Combination Sum II
#

# @lc code=start
class Solution:
    def comb(self, pos: int, rem: int) -> list:
        if rem == 0:
            return [[]]
        if pos == len(self.cands):
            return []
        
        output = [] 
        for i in range(pos, len(self.cands)):
            if i > pos and self.cands[i - 1] == self.cands[i]:
                continue
            if self.cands[i] > rem:
                break
                
            for nxt in self.comb(i + 1, rem - self.cands[i]):
                output.append(nxt + [self.cands[i]])
        
        return output

    def combinationSum2(self, candidates: list, target: int) -> list:
        self.cands = [i for i in sorted(candidates) if i <= target]

        return self.comb(0, target)

# obj = Solution()
# obj.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8)
# @lc code=end
