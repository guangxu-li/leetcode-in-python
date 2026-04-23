#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#


# @lc code=start
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        def combination() -> list[list[int]]:
            partials = [[]]
            ans = set()
            for num in nums:
                for i in range(len(partials)):
                    candidate = partials[i] + [num]
                    if len(candidate) < 3:
                        partials.append(candidate)
                    elif sum(candidate) == 0:
                        ans.add(tuple(sorted(candidate)))
            return list(ans)

        def twosum_twopointers() -> list[list[int]]:
            nums.sort()
            n = len(nums)
            ans = set()
            for i in range(n - 2):
                lo = i + 1
                hi = n - 1
                target = -nums[i]
                while lo < hi:
                    val = nums[lo] + nums[hi]
                    if val < target:
                        lo += 1
                    elif val > target:
                        hi -= 1
                    else:
                        ans.add((nums[i], nums[lo], nums[hi]))
                        lo += 1
                        hi -= 1
            return list(ans)

        def twosum_map() -> list[list[int]]:
            n = len(nums)
            ans = set()
            for i in range(n - 2):
                target = -nums[i]
                numset = set()
                for j in range(i + 1, n):
                    val = target - nums[j]
                    if val in numset:
                        ans.add(tuple(sorted((nums[i], nums[j], val))))
                    numset.add(nums[j])

            return list(ans)

        # return combination()
        # return twosum_twopointers()
        return twosum_map()


# @lc code=end
