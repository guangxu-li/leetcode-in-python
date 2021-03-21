#
# @lc app=leetcode id=535 lang=python3
#
# [535] Encode and Decode TinyURL
#

# @lc code=start
import random


class Codec:
    base = "0123456789ABCDEFGHIJKLMNOPGRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

    def __init__(self):
        self.host = "http://tinyurl.com/"
        self.mapping = dict()

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        key = ""
        for i in range(6):
            key += self.base[random.randrange(len(self.base))]
        self.mapping[key] = longUrl
        
        return self.host + key

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.mapping[shortUrl.removeprefix(self.host)]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
# @lc code=end

