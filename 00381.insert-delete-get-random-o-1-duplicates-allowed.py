#
# @lc app=leetcode id=381 lang=python3
#
# [381] Insert Delete GetRandom O(1) - Duplicates allowed
#

# @lc code=start
from collections import defaultdict
from random import choice


class RandomizedCollection:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.vals_idx = defaultdict(set)
        self.nums = []

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        """
        self.vals_idx[val].add(len(self.nums))
        self.nums.append(val)

        return len(self.vals_idx[val]) == 1

    def remove(self, val: int) -> bool:
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        """
        if not self.vals_idx[val]:
            return False

        rm_idx, last = self.vals_idx[val].pop(), self.nums[-1]
        # add before discard -> when rm_idx is at the end of the list
        self.vals_idx[last].add(rm_idx)
        self.vals_idx[last].discard(len(self.nums) - 1)
        self.nums[rm_idx] = last
        self.nums.pop()

        return True

    def getRandom(self) -> int:
        """
        Get a random element from the collection.
        """
        return choice(self.nums)


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
# @lc code=end
