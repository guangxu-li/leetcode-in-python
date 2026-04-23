#
# @lc app=leetcode id=1756 lang=python3
#
# [1756] Design Most Recently Used Queue
#


# @lc code=start
from math import floor


class MRUQueue:
    def __init__(self, n: int):
        self.bucket_size = floor(n**0.5)
        self.buckets_start = []
        self.buckets = []

        for i in range(1, n + 1):
            self._append(i)

    def _pop(self, bucket_idx: int, offset: int) -> int:
        bucket = self.buckets[bucket_idx]
        val = bucket.pop(offset)

        for i in range(bucket_idx + 1, len(self.buckets_start)):
            self.buckets_start[i] -= 1

        if not bucket:
            self.buckets.pop(bucket_idx)
            self.buckets_start.pop(bucket_idx)

        return val

    def _append(self, val: int):
        if not self.buckets:
            self.buckets_start.append(0)
            self.buckets.append([val])
        elif len(self.buckets[-1]) == self.bucket_size:
            self.buckets_start.append(self.buckets_start[-1] + len(self.buckets[-1]))
            self.buckets.append([val])
        else:
            self.buckets[-1].append(val)

    def fetch(self, k: int) -> int:
        # 1. binary search bucket_start to find the target buckets
        # 2. bucket[k - i] is the answer:
        # 3. remove it from the bucket and decrease all bucket_start with larger number buckets
        # 4. append to the last bucket

        lo, hi = 0, len(self.buckets_start)
        while lo < hi:
            mid = (lo + hi) >> 1
            if self.buckets_start[mid] >= k:
                hi = mid
            else:
                lo = mid + 1

        # lo is the first one >= k, which means there're >= k elements on the left side of buckets[lo]
        i = lo - 1
        val = self._pop(i, k - self.buckets_start[i] - 1)
        self._append(val)

        return val


# Your MRUQueue object will be instantiated and called as such:
# obj = MRUQueue(n)
# param_1 = obj.fetch(k)
# @lc code=end
