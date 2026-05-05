#
# @lc app=leetcode id=722 lang=python3
#
# [722] Remove Comments
#

# @lc code=start
class Solution:
    def removeComments(self, source: list[str]) -> list[str]:
        output, block = [], False

        for line in source:
            newline, i = newline if block else "", 0
            while i < len(line) and (block or line[i : i + 2] != "//"):
                if line[i : i + 2] == "/*" and not block:
                    block = True
                    i += 2
                elif line[i : i + 2] == "*/" and block:
                    block = False
                    i += 2
                else:
                    newline += "" if block else line[i]
                    i += 1

            if newline and not block:
                output.append(newline)

        return output


# @lc code=end
