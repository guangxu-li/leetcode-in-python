#
# @lc app=leetcode id=355 lang=python3
#
# [355] Design Twitter
#

# @lc code=start
from collections import defaultdict
from itertools import islice, chain
import heapq


class Twitter:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.posts = defaultdict(list)
        self.followers = defaultdict(set)
        self.timer = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        self.posts[userId].append((self.timer, tweetId))
        self.timer -= 1

    def getNewsFeed(self, userId: int) -> list[int]:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        feeds = chain(*(self.posts[id] for id in self.followers[userId] | {userId}))
        return [feed for _, feed in heapq.nsmallest(10, feeds)]

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        self.followers[followerId].discard(followeeId)


obj = Twitter()
obj.postTweet(1, 5)
obj.postTweet(1, 3)
print(obj.getNewsFeed(1))
# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
# @lc code=end
