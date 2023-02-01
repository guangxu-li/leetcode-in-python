#
# @lc app=leetcode id=1626 lang=python3
#
# [1626] Best Team With No Conflicts
#

# @lc code=start
from bisect import bisect_left
from collections import defaultdict
from functools import lru_cache
from typing import List


class Solution:
    # @age: current age group
    # @lower_bound: the selected scores must be larger than the lower_bound
    @lru_cache(None)
    def best_team_score(self, age: int, lower_bound: int) -> int:
        if age == len(self.age_scores):
            return 0

        _max = self.best_team_score(age + 1, lower_bound)  # skip this age group

        _sum = 0
        scores = self.age_scores[age]
        i = bisect_left(scores, lower_bound)
        for j in range(i, len(scores)):
            score = scores[j]
            _sum += score
            _max = max(_max, _sum + self.best_team_score(age + 1, score))

        return _max

    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        age2scores = defaultdict(list)
        for age, score in sorted(zip(ages, scores)):
            age2scores[age].append(score)

        self.age_scores = []
        self.age_scores = list(age2scores.values())
        for _, scores in age2scores.items():
            if self.age_scores and self.age_scores[-1][-1] <= scores[0]:
                self.age_scores[-1].extend(scores) # compress two age groups together
            else:
                self.age_scores.append(scores)

        return self.best_team_score(0, 0)


# @lc code=end
