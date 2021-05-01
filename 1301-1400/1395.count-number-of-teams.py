#
# @lc app=leetcode id=1395 lang=python3
#
# [1395] Count Number of Teams
#

# @lc code=start
class Solution:
    def update(self, bit: list[int], i: int, diff: int) -> None:
        while i < len(bit):
            bit[i] += diff
            i += i & -i

    def query(self, bit: list[int], i: int, j: int) -> None:
        cnt = 0
        while j > i:
            cnt += bit[j]
            j -= j & -j
        while i > j:
            cnt -= bit[i]
            i -= i & -i

        return cnt

    def numTeams(self, rating: list[int]) -> int:
        a, b = min(rating), max(rating)
        bit_left, bit_right = [0] * (b - a + 2), [0] * (b - a + 2)

        for r in rating:
            self.update(bit_right, r - a + 1, 1)

        cnt = 0
        for r in rating:
            self.update(bit_right, r - a + 1, -1)
            cnt += self.query(bit_left, 0, r - a) * self.query(
                bit_right, r - a + 1, len(bit_right) - 1
            )
            cnt += self.query(bit_right, 0, r - a) * self.query(
                bit_left, r - a + 1, len(bit_left) - 1
            )
            self.update(bit_left, r - a + 1, 1)

        return cnt


# @lc code=end
