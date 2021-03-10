#
# @lc app=leetcode id=1244 lang=python3
#
# [1244] Design A Leaderboard
#

# @lc code=start
from collections import defaultdict
import random


class Leaderboard:

    def __init__(self):
        self.players = defaultdict(int)        

    def addScore(self, playerId: int, score: int) -> None:
        self.players[playerId] += score
    
    def __partition(self, scores: List[int], lo: int, hi: int, pivot: int) -> int:
        pivot_val = scores[pivot]
        scores[pivot], scores[hi] = scores[hi], scores[pivot]
        
        j = lo
        for i in range(lo, hi + 1):
            if scores[i] > pivot_val:
                scores[i], scores[j] = scores[j], scores[i]
                j += 1
        
        scores[j], scores[hi] = scores[hi], scores[j]

        return j
        
    def __quickselect(self, scores: List[int], lo: int, hi: int, k: int) -> None:
        if lo == hi:
            return
        
        pivot = self.__partition(scores, lo, hi, random.randrange(lo, hi))

        if pivot < k:
            self.__quickselect(scores, pivot + 1, hi, k)
        elif pivot == k:
            return
        elif pivot > k:
            self.__quickselect(scores, lo, pivot - 1, k)
        
    def top(self, K: int) -> int:
        scores = list(self.players.values())
        self.__quickselect(scores, 0, len(scores) - 1, K - 1)
        return sum(scores[i] for i in range(K))
        
    def reset(self, playerId: int) -> None:
        self.players[playerId] = 0


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)
# @lc code=end

