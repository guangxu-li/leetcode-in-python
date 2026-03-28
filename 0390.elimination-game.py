#
# @lc app=leetcode id=390 lang=python3
#
# [390] Elimination Game
#

# @lc code=start
class Solution:
    def lastRemaining(self, n: int) -> int:
        # 1 + n // 2 for rem of reverse order delete
        return 1 if n == 1 else 2 * (1 + n // 2 - self.lastRemaining(n // 2))        
# @lc code=end
