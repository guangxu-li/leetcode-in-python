#
# @lc app=leetcode id=631 lang=python3
#
# [631] Design Excel Sum Formula
#

# @lc code=start


from collections import defaultdict


class Excel:
    def __init__(self, H: int, W: str):
        W = ord(W) - ord("A") + 1
        self.cells = [[{"val": 0, "formula": None} for i in range(W)] for j in range(H)]

    def set(self, r: int, c: str, v: int) -> None:
        r, c = r - 1, ord(c) - ord("A")
        self.cells[r][c] = {"val": v, "formula": None}

    def get(self, r: int, c: str) -> int:
        r, c = r - 1, ord(c) - ord("A")
        cell = self.cells[r][c]
        counter = cell["formula"]

        return (
            sum(self.get(*pos) * times for pos, times in counter.items())
            if counter
            else cell["val"]
        )

    def sum(self, r: int, c: str, strs: list[str]) -> int:
        _r, _c = r - 1, ord(c) - ord("A")
        counter = defaultdict(int)
        for s in strs:
            start, end = s.split(":") if len(s) > 3 else (s, s)

            for i in range(int(start[1:]), int(end[1:]) + 1):
                for j in range(ord(start[0]) - ord("A"), ord(end[0]) - ord("A") + 1):
                    counter[(i, chr(j + ord("A")))] += 1

        self.cells[_r][_c]["formula"] = counter
        return self.get(r, c)


# Your Excel object will be instantiated and called as such:
# obj = Excel(H, W)
# obj.set(r,c,v)
# param_2 = obj.get(r,c)
# param_3 = obj.sum(r,c,strs)
# @lc code=end
