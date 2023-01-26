#
# @lc app=leetcode id=2402 lang=python3
#
# [2402] Meeting Rooms III
#

# @lc code=start
import heapq
from typing import List


# Maintain two min heaps:
#   1. ready room number
#   2. (room end time, booked room number)
#
# For each meeting:
#   1. Return the booked rooms to the ready rooms if the meeting is already ended based on the current start time.
#   2. If there's any available room, then use the available room.
#   3. Otherwise, use the earliest available booked room.
#       - We have a delay here to wait for the room being available.
#       - delay = start - earliest_booked_end_time
#       - the new ned time would be end_time + delay
#   4. update the used room counter for this meeting
class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        ready = list(range(n))  # sorted, so no need to heapify
        booked = []  # min heap based on end time. (10, 0) -> (end time, room number)
        counter = [0] * n

        for start, end in sorted(meetings):
            while booked and booked[0][0] <= start:
                _, room = heapq.heappop(booked)
                heapq.heappush(ready, room)

            if ready:
                room = heapq.heappop(ready)
                heapq.heappush(booked, (end, room))
            else:
                available_time, room = heapq.heappop(booked)
                heapq.heappush(booked, (end + available_time - start, room))  # available_time - start is the delay time

            counter[room] += 1

        return counter.index(max(counter))


# @lc code=end
