#
# @lc app=leetcode id=690 lang=python3
#
# [690] Employee Importance
#

# @lc code=start
"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""
from collections import defaultdict, deque


class Solution:
    def getImportance(self, employees: list["Employee"], id: int) -> int:
        graph = defaultdict(lambda: Employee(None, 0, []), [(e.id, e) for e in employees])
        subordinates, importance = deque([id]), 0
        while subordinates:
            e = graph[subordinates.popleft()]
            importance += e.importance
            subordinates.extend(e.subordinates)

        return importance


# @lc code=end
