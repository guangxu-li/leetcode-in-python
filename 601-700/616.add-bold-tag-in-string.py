#
# @lc app=leetcode id=616 lang=python3
#
# [616] Add Bold Tag in String
#

# @lc code=start
from re import escape, finditer


class Solution:
    def merge_spans(self, spans: list[list[int]]) -> list[list[int]]:
        overlap = lambda a, b: a[0] <= b[1] and a[1] >= b[0]

        output = []
        for span in spans:
            if output and overlap(output[-1], span):
                output[-1] = [min(output[-1][0], span[0]), max(output[-1][1], span[1])]
            else:
                output.append(span)

        return output

    def addBoldTag(self, s: str, dict: list[str]) -> str:
        pattern = r"(?=({}))".format("|".join(map(escape, sorted(dict, key=len, reverse=True))))
        spans = self.merge_spans([m.span(1) for m in finditer(pattern, s) if m.group(1)])

        for i, span in enumerate(spans):
            span = [span[0] + i * 7, span[1] + i * 7]
            s = s[: span[0]] + "<b>" + s[span[0] : span[1]] + "</b>" + s[span[1] :]

        return s


# @lc code=end
