#
# @lc app=leetcode id=696 lang=python3
#
# [696] Count Binary Substrings
#

# @lc code=start
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        cnt, prev_cnt, cur_cnt, cur = 0, 0, 0, s[0]
        for bit in s:
            if bit == cur:
                cur_cnt += 1
            else:
                cnt += min(prev_cnt, cur_cnt)
                prev_cnt, cur_cnt, cur = cur_cnt, 1, bit
            
        return cnt + min(prev_cnt, cur_cnt)
            
# @lc code=end

