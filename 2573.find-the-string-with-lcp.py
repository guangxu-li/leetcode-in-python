#
# @lc app=leetcode id=2573 lang=python3
#
# [2573] Find the String with LCP
#


# @lc code=start
class Solution:
    def findTheString(self, lcp: List[List[int]]) -> str:
        n = len(lcp)
        lcp = [[lcp[i][j] if i < n and j < n else 0 for j in range(n + 1)] for i in range(n + 1)]
        word = [""] * n
        cur = ord("a")
        for i in range(n):
            if word[i]:
                continue
            if cur > ord("z"):
                return ""
            for j in range(i, n):
                word[j] = chr(cur) if lcp[i][j] else word[j]
            cur += 1

        for i in reversed(range(n)):
            for j in reversed(range(n)):
                expect = 1 + lcp[i + 1][j + 1] if word[i] == word[j] else 0
                if lcp[i][j] != expect:
                    return ""
        return "".join(word)


# @lc code=end
