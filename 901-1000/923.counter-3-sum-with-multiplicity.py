#
# @lc app=leetcode id=923 lang=python3
#
# [923] 3Sum With Multiplicity
#

# @lc code=start
from collections import Counter
from itertools import combinations_with_replacement as cwr


class Solution:
    def threeSumMulti(self, arr: list[int], target: int) -> int:
        counter, cnt, mod = Counter(arr), 0, 10 ** 9 + 7
        for i, j in cwr(counter, 2):
            k = target - i - j
            if i == j == k:
                cnt = (
                    cnt + counter[i] * (counter[i] - 1) * (counter[i] - 2) // 6
                ) % mod
            elif i == j != k:
                cnt = (cnt + counter[i] * (counter[i] - 1) // 2 * counter[k]) % mod
            elif k > i and k > j:
                cnt = (cnt + counter[i] * counter[j] * counter[k]) % mod
        
        return cnt


# @lc code=end
