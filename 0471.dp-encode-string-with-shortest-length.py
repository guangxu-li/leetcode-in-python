#
# @lc app=leetcode id=471 lang=python3
#
# [471] Encode String with Shortest Length
#

# @lc code=start
class Solution:
    def longest_common_pre_suf(self, W: str) -> int:
        dp = [0] * len(W)

        for i in range(1, len(W)):
            j = dp[i - 1]
            while j > 0 and W[i] != W[j]:
                j = dp[j - 1]
            
            dp[i] = j + (W[i] == W[j])
            
        return dp[-1]

    def encode(self, s: str) -> str:
        dp = [["" for _ in range(len(s))] for _ in range(len(s))]

        for _len in range(len(s)):
            for i in range(len(s) - _len):
                j = i + _len
                dp[i][j] = s[i:j + 1]

                if _len < 3:
                    continue

                len_repeat = self.longest_common_pre_suf(dp[i][j])
                k = _len + 1 - len_repeat
                if len_repeat and not (_len + 1) % k:
                    dp[i][j] = str((_len + 1) // k) + "[" + dp[i][i + k - 1] + "]"
                else:
                    dp[i][j] = min([dp[i][k] + dp[k + 1][j] for k in range(i, j)], key=len)

        return dp[0][-1]
# @lc code=end
