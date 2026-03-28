#
# @lc app=leetcode id=1081 lang=python3
#
# [1081] Smallest Subsequence of Distinct Characters
#

# @lc code=start
class Solution:
    def smallestSubsequence(self, s: str) -> str:
        """
        1. Find first decreasing index and remove it
        2. Only remove if the potential removed element is not the last occurrence
        3. If the cur char already used, skip this one.
        4. eg: accb -> we skip the second c. If the following char is capcable to pop
           the last char in output when we skip then it should also be capcable to pop
           the skipped char, which means the char already used no need to consider about
           it
        """
        last, output, used = {chs: i for i, chs in enumerate(s)}, [], set()
        for i, chs in enumerate(s):
            if chs in used:
                continue
            while output and last[output[-1]] > i and output[-1] > chs:
                used.remove(output.pop())

            used.add(chs)
            output.append(chs)

        return "".join(output)


# @lc code=end
