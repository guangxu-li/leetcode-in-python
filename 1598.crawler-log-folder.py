#
# @lc app=leetcode id=1598 lang=python3
#
# [1598] Crawler Log Folder
#

# @lc code=start
class Solution:
    def minOperations(self, logs: list[str]) -> int:
        depth = 0
        for log in logs:
            depth += 1 if log[0] != "." else 2 - len(log)
            depth = max(0, depth)

        return depth
# @lc code=end
