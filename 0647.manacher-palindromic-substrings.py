#
# @lc app=leetcode id=647 lang=python3
#
# [647] Palindromic Substrings
#

# @lc code=start
class Solution:
    def countSubstrings(self, s: str) -> int:
        s = "^#" + "#".join(s) + "#$"
        p = [0] * len(s)

        bound = center = cnt = 0
        for i in range(1, len(p) - 1):
            if i < bound:
                p[i] = min(p[2 * center - i], bound - i)
            
            while s[i - p[i] - 1] == s[i + p[i] + 1]:
                p[i] += 1
            
            if i + p[i] > bound:
                bound, center = i + p[i], i
            
            cnt += (p[i] + 1) // 2
        
        return cnt
# @lc code=end

