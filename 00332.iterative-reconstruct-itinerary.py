#
# @lc app=leetcode id=332 lang=python3
#
# [332] Reconstruct Itinerary
#

# @lc code=start
from collections import defaultdict


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # Path: Eulerian path (with one deadend)
        # Cycle: Eulerian Cycle
        #
        # Lexicographical order:
        #   1. path
        #   2. cycle
        #   3. path + path (no solution)
        #   4. path + cycle (path should be the last part of the itinerary)
        #   5. cycle + cycle = cycle
        #   6. cycle + path = path (start = cycle start, end = path end)
        #   7. path + path + path (no solution)
        #   8. path + path + cycle (no solution)
        #   9. path + cycle + path (no solution)
        #  10. path + cycle + cycle = path + cycle
        #  11. cycle + path + path (no solution)
        #  12. cycle + path + cycle = path + cycle
        #  13. cycle + cycle + path = cycle + path = path
        #  14. cycle + cycle + cycle = cycle

        # stack St;
        # put start vertex in St;
        # until St is empty
        #   let V be the value at the top of St;
        #   if degree(V) = 0, then
        #     add V to the answer;
        #     remove V from the top of St;
        #   otherwise
        #     find any edge coming out of V;
        #     remove it from the graph;
        #     put the second end of this edge in St;

        graph = defaultdict(list)
        for departure, arrival in sorted(tickets, reverse=True):
            graph[departure].append(arrival)

        # JFK -> KUL
        # JFK -> NRT -> JFK
        #
        # stack: JFK, KUL
        #        JFK, NRT, JFK
        itinerary = []
        stack = ["JFK"]
        while stack:
            while arrivals := graph[stack[-1]]:
                stack.append(arrivals.pop())
            itinerary.append(stack.pop())

        # implementation like pseudocode
        # while stack:
        #     if arrivals := graph[stack[-1]]:
        #         stack.append(arrivals.pop())
        #     else:
        #         itinerary.append(stack.pop())

        return itinerary[::-1]

# @lc code=end
