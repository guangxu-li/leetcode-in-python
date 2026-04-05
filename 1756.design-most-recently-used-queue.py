#
# @lc app=leetcode id=1756 lang=python3
#
# [1756] Design Most Recently Used Queue
#


# @lc code=start
class BIT:
    def __init__(self, cap: int):
        cap += 1
        self.tree = [0] * cap
        self.cap = cap

    def update(self, i: int, delta: int):
        while i < self.cap:
            self.tree[i] += delta
            i += i & -i

    # smallest index with prefix >= target
    def lower_bound(self, target: int) -> int:
        _sum, i = 0, 0
        for step in reversed(range(self.cap.bit_length())):
            ni = i + (1 << step)
            if ni < self.cap and _sum + self.tree[ni] < target:
                _sum += self.tree[ni]
                i = ni
        return i + 1


class MRUQueue:
    def __init__(self, n: int):
        self.bit = BIT(n + 2000)
        self.vals = [0] * (n + 1)
        for i in range(1, n + 1):
            self.bit.update(i, 1)
            self.vals[i] = i

    def fetch(self, k: int) -> int:
        i = self.bit.lower_bound(k)
        val = self.vals[i]

        self.vals[i] = 0
        self.vals.append(val)

        self.bit.update(i, -1)
        self.bit.update(len(self.vals) - 1, 1)

        return val


# Your MRUQueue object will be instantiated and called as such:
# obj = MRUQueue(n)
# param_1 = obj.fetch(k)
# @lc code=end
