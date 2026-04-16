#
# @lc app=leetcode id=271 lang=python3
#
# [271] Encode and Decode Strings
#


# @lc code=start
from typing import List


class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string."""
        encoded = []
        for s in strs:
            encoded.append(str(len(s)))
            encoded.append("#")
            encoded.append(s)
        return "".join(encoded)

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings."""
        buffer = []
        decoded = []
        i = 0
        while i < len(s):
            if s[i] == "#":
                length = int("".join(buffer))
                decoded.append(s[i + 1 : i + 1 + length])
                buffer = []
                i += 1 + length
            else:
                buffer.append(s[i])
                i += 1

        return decoded


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
# @lc code=end
