#
# @lc app=leetcode id=246 lang=python3
#
# [246] Strobogrammatic Number
#

# @lc code=start
class Solution:
    mapping = dict({"0": "0", "1": "1", "6": "9", "8": "8", "9": "6"})

    def isStrobogrammatic(self, num: str) -> bool:
        for i in range((len(num) + 1) // 2):
            if num[i] not in self.mapping or self.mapping[num[i]] != num[-i - 1]:
                return False

        return True

print(Solution().isStrobogrammatic("69"))
# @lc code=end
