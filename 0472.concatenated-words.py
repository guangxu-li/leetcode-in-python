#
# @lc app=leetcode id=472 lang=python3
#
# [472] Concatenated Words
#

# @lc code=start
from collections import defaultdict
from functools import reduce
from typing import List


class Solution:
    # multi means whether or not it's allowed to match the word with a single one word.
    #   - multi == True: we must concatenate multiple words to match the word
    #   - multi == False: no restriction
    def find(self, word: str, multi: bool = True) -> bool:
        h = self.root
        for i, w in enumerate(word):
            h = h[w]
            if not h:
                return False

            if "END" not in h:
                continue

            if self.find(word[i + 1 :], False):
                return True

        return "END" in h and not multi

    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        Trie = lambda: defaultdict(Trie)
        self.root = Trie()

        for word in words:
            reduce(dict.__getitem__, word, self.root)["END"] = word

        return filter(self.find, words)


# @lc code=end
