#
# @lc app=leetcode id=923 lang=python3
#
# [923] 3Sum With Multiplicity
#

# @lc code=start
class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        mod = 10**9 + 7
        cnt = 0
        arr.sort()
        
        for i in range(len(arr)):
            t = target - arr[i]
            j, k = i + 1, len(arr) - 1

            while j < k:
                left, right = arr[j], arr[k]
                sum = left + right
                if sum < t:
                    j += 1
                elif sum > t:
                    k -= 1
                elif arr[j] != arr[k]:
                    cnt_left, cnt_right = 0, 0
                    while arr[j] == left:
                        cnt_left += 1
                        j += 1
                    while arr[k] == right:
                        cnt_right += 1
                        k -= 1
                    cnt = (cnt + cnt_left * cnt_right) % mod
                else:
                    n = k + 1 - j
                    cnt = (cnt + n * (n - 1) // 2) % mod
                    j = k
        
        return cnt
# @lc code=end

