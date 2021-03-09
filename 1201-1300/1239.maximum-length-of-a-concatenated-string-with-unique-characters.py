#
# @lc app=leetcode id=1239 lang=python3
#
# [1239] Maximum Length of a Concatenated String with Unique Characters
#

# @lc code=start
class Solution:
    def maxLength(self, arr: List[str]) -> int:
        filtered = [set(str) for str in arr if len(str) == len(set(str))]

        found = [set()]
        for s1 in filtered:
            for s2 in found:
                if not (s1 & s2):
                    found.append(s1 | s2)
        
        return max([len(i) for i in found])
            
# @lc code=end

