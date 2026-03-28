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

        # procedure FindEulerPath(V)
        #   1. iterate through all the edges outgoing from vertex V;
        #       - remove this edge from the graph
        #       - and call FindEulerPath from the second end of this edge;
        #   2. add vertex V to the answer.

        # JFK -> KUL
        # JFK -> NRT -> JFK
        #
        # Traverse before output
        # Traverse:
        #   1. JFK -> KUL: KUL, JFK
        #   2. JFK -> NRT -> JFK: JFK, NRT, JFK
        # Reverse: JFK, NRT, JFK, KUL
        graph = defaultdict(list)
        for departure, arrival in sorted(tickets, reverse=True):
            graph[departure].append(arrival)

        itinerary = []
        def traverse(departure):
            while arrivals := graph[departure]:
                traverse(arrivals.pop())
            itinerary.append(departure)

        traverse("JFK")
        return itinerary[::-1]

# @lc code=end
