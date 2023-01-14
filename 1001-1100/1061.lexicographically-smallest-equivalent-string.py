#
# @lc app=leetcode id=1061 lang=python3
#
# [1061] Lexicographically Smallest Equivalent String
#


# Constraints:
# 1 <= s1.length, s2.length, baseStr <= 1000
# s1.length == s2.length
# s1, s2, and baseStr consist of lowercase English letters.

# @lc code=start

# According to the problem description, each character is able to find a smallest equivalent
# character. So we can treat this smallest equivalent character as one parent of disjoint set union.

class UnionFind:
    def __init__(self):
        self.parents = list(range(26))

    def find(self, i: int) -> int:
        if self.parents[i] == i:
            return i

        return self.find(self.parents[i])

    def union(self, i, j: int) -> None:
        i = self.find(i)
        j = self.find(j)

        i, j = sorted([i, j])
        self.parents[j] = i


class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        ch2int = lambda ch: ord(ch) - ord("a")
        int2ch = lambda i: chr(i + ord("a"))

        uf = UnionFind()
        for ch1, ch2 in zip(s1, s2):
            i, j = ch2int(ch1), ch2int(ch2)
            uf.union(i, j)

        return "".join(int2ch(uf.find(i)) for i in map(ch2int, baseStr))


# @lc code=end
