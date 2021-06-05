#
# @lc app=leetcode id=302 lang=python3
#
# [302] Smallest Rectangle Enclosing Black Pixels
#

# @lc code=start
class Solution:
    def left_most(self, image: list[list[str]], lo: int, hi: int) -> int:
        while lo <= hi:
            mid = (lo + hi) >> 1

            if any(image[x][mid] == "1" for x in range(len(image))):
                hi = mid - 1
            else:
                lo = mid + 1

        return lo

    def right_most(self, image: list[list[str]], lo: int, hi: int) -> int:
        while lo <= hi:
            mid = (lo + hi) >> 1

            if any(image[x][mid] == "1" for x in range(len(image))):
                lo = mid + 1
            else:
                hi = mid - 1

        return hi

    def minArea(self, image: list[list[str]], x: int, y: int) -> int:
        image_tran = list(zip(*image))

        left, right = self.left_most(image, 0, y), self.right_most(image, y, len(image[0]) - 1)
        top, bottom = self.left_most(image_tran, 0, x), self.right_most(
            image_tran, x, len(image) - 1
        )

        print(left, right, top, bottom)
        return (right - left + 1) * (bottom - top + 1)


# @lc code=end
