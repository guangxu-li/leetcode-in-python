#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#


# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        s1, s2 = min(strs), max(strs)
        s3 = []
        for ch1, ch2 in zip(s1, s2):
            if ch1 != ch2:
                break
            s3.append(ch1)
        return "".join(s3)


# @lc code=end
