#
# @lc app=leetcode id=2467 lang=python3
#
# [2467] Most Profitable Path in a Tree
#

# @lc code=start
from collections import defaultdict, deque
from typing import DefaultDict, List


# Several important conclusions from the description:
#   - no circle in the graph
#   - given any pair of nodes there's exactly one path to connect them.
#
# 1. find the bob's path first. And build a map that maps from the node to bob's arrival time.
# 2. find all alice path and calculate the total profit.
class Solution:
    # root_path finds the path starts from the `start` to the `root`.
    # It assumes that there only one path exist.
    # If no path exists, it returns None.
    def root_path(self, start: int) -> List[int]:
        q = deque([[start]])
        visited = {start}
        while q:
            path = q.popleft()
            curr = path[-1]
            for next in self.graph[curr] - visited:
                new_path = path + [next]
                if next == 0:
                    return new_path
                visited.add(next)
                q.append(new_path)

        return None

    def income(self, node, time: int) -> int:
        if node not in self.bob_arrival_time:
            # bob won't pass this node
            return self.amount[node]

        bob_time = self.bob_arrival_time[node]
        if time < bob_time:
            return self.amount[node]
        elif time == bob_time:
            return self.amount[node] // 2
        else:
            return 0

    def alice_move(self) -> int:
        _max = -float("inf")
        q = deque([(0, 0, self.amount[0])])  # (node, time, profit including the node)
        while q:
            curr, time, profit = q.popleft()
            adjs = self.graph[curr]
            if len(adjs) == 0:
                _max = max(_max, profit)
            for next in adjs:
                self.graph[next].remove(curr)
                q.append((next, time + 1, profit + self.income(next, time + 1)))

        return _max

    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        self.amount = amount
        self.graph = defaultdict(set)
        for u, v in edges:
            self.graph[u].add(v)
            self.graph[v].add(u)

        bob_path = self.root_path(bob)  # path from bob to 0
        self.bob_arrival_time = {node: i for i, node in enumerate(bob_path)}  # node to bob arrival time
        # print(self.bob_arrival_time)

        return self.alice_move()


# @lc code=end
