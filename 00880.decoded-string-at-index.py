#
# @lc app=leetcode id=880 lang=python3
#
# [880] Decoded String at Index
#

# @lc code=start
class Solution:
    def decodeAtIndex(self, S: str, K: int) -> str:
        cnt = 0
        for i, ch in enumerate(S):
            cnt = cnt * int(ch) if ch.isdigit() else cnt + 1
            if cnt >= K:
                break
        
        for ch in S[i::-1]:
            if ch.isdigit():
                cnt /= int(ch)
                K %= cnt
            else:
                if K == cnt or not K:
                    return ch
                cnt -= 1
# @lc code=end
