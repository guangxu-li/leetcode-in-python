#
# @lc app=leetcode id=642 lang=python3
#
# [642] Design Search Autocomplete System
#

# @lc code=start
from collections import defaultdict


class AutocompleteSystem:
    def __init__(self, sentences: List[str], times: List[int]):
        self.words: str = ""
        self.records = defaultdict(int)
        self.records.update(zip(sentences, times))

    def input(self, c: str) -> List[str]:
        if c == "#":
            self.records[self.words] += 1
            self.words = ""
        else:
            self.words += c
            records = [
                k
                for k, _ in sorted(
                    self.records.items(), key=lambda item: (-item[1], item[0])
                )
                if k.startswith(self.words)
            ]

            return records[: min(len(records), 3)]


# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)
# @lc code=end
