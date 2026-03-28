#
# @lc app=leetcode id=402 lang=python3
#
# [402] Remove K Digits
#

# @lc code=start
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        output = []
        for digit in num:
            while output and k and output[-1] > digit:
                output.pop()
                k -= 1
            output.append(digit)
        
        return str(int("0" + "".join(output[:len(output) - k])))
# @lc code=end
