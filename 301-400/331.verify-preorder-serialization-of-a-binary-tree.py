#
# @lc app=leetcode id=331 lang=python3
#
# [331] Verify Preorder Serialization of a Binary Tree
#

# @lc code=start
class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        slots = 1
        for node in preorder.split(","):
            if not slots:
                return False
            slots += -1 if node == "#" else 1
        
        return not slots
# @lc code=end
