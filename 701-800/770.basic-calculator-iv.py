#
# @lc app=leetcode id=770 lang=python3
#
# [770] Basic Calculator IV
#

# @lc code=start
from collections import Counter
from re import sub


class Vars(Counter):
    def __add__(self, other):
        self.update(other)
        return self

    def __sub__(self, other):
        self.subtract(other)
        return self

    def __mul__(self, other):
        product = Vars()
        for a in self:
            for b in other:
                product[tuple(sorted(a + b))] += self[a] * other[b]

        return product


class Solution:
    def basicCalculatorIV(
        self, expression: str, evalvars: list[str], evalints: list[int]
    ) -> list[str]:
        vals = dict(zip(evalvars, evalints))
        calc = lambda var: Vars({(var,): 1} if var.isalpha() else {(): int(var)})

        res = eval(sub("(\w+)", r'calc(str(vals.get("\1", "\1")))', expression))
        return [
            "*".join((str(res[k]),) + k)
            for k in sorted(res, key=lambda k: (-len(k), k))
            if res[k]
        ]
