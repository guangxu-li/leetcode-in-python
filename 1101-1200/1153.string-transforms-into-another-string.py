#
# @lc app=leetcode id=1153 lang=python3
#
# [1153] String Transforms Into Another String
#

# @lc code=start
class Solution:
    def canConvert(self, str1: str, str2: str) -> bool:
        mapping = dict()
        return (
            str1 == str2
            or len(set(str2)) < 26
            and all(mapping.setdefault(ch1, ch2) == ch2 for ch1, ch2 in zip(str1, str2))
        )


# @lc code=end
