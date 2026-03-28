#
# @lc app=leetcode id=354 lang=python3
#
# [354] Russian Doll Envelopes
#

# @lc code=start
import bisect

class Solution:
    def maxEnvelopes(self, envelopes: list[list[int]]) -> int:
        """transform to find longest increasing subsequence"""
        heights = [j for _, j in sorted(envelopes, key=lambda e: (e[0], -e[1]))]

        asc_subseq = []
        for height in heights:
            i = bisect.bisect_left(asc_subseq, height)
            if i == len(asc_subseq):
                asc_subseq.append(height)
            else:
                asc_subseq[i] = height
        
        return len(asc_subseq)
# @lc code=end

