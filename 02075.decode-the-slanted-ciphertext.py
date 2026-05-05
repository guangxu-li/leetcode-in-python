#
# @lc app=leetcode id=2075 lang=python3
#
# [2075] Decode the Slanted Ciphertext
#


# @lc code=start
class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        text, plaintext, cols = encodedText, [], len(encodedText) // rows
        for i in range(cols):
            for j in range(rows):
                idx = j * cols + j + i
                if idx < len(text):
                    plaintext.append(text[idx])

        return "".join(plaintext).rstrip()


# @lc code=end
