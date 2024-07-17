from heapq import heapify, heappop
from collections import defaultdict


# @leet start
class Twitter:
    """
    This class designs a simplified version of twitter, where users
    post tweets, follow/unfollow each other, and can see the 10 most recent
    tweets in their news feed, based on who they follow.

    To design this class, we need to have a key value mapping of userId -> following
    As well, that should also support fast removal, since unfollows should be quick.
    So, we have a defaultdict(set) for that.

    For the tweets, we want to order them chronologically, but there is no timestamp provided.
    We use a monotonically increasing timestamp for this.
    As well, we want to be able to access a user's tweets quickly. We can use a dict for this
    and place tuples of timestamp, tweet_id into it. Since we know that timestamps are
    increasing, this is always sorted without needing to use a tree data structure.

    Finally, in getNewsFeed, we iterate through all of the users that userId is following
    and the userId itself, and add the 10 latest tweets to a heap.
    We then pop the heap up to 10 times, and return the tweet_ids in the heap.

    This means that all operations are constant time except for getting the news feed,
    which is $O(n\log{}m)$.

    Twitter in reality uses a background worker to write a newsfeed in the background,
    so accessing the news feed would be constant time, and updating is still constant time,
    but fires off these background workers to materialize a news feed for a given user.
    """

    def __init__(self):
        self.followers = defaultdict(set)
        self.tweets = defaultdict(list)
        self.timestamp = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((-self.timestamp, tweetId))
        self.timestamp += 1

    def getNewsFeed(self, userId: int) -> list[int]:
        heap = []

        for following in self.followers[userId]:
            heap.extend(self.tweets[following][-10:])

        # add in the user's own tweets
        heap.extend(self.tweets[userId][-10:])
        heapify(heap)
        res = []
        for _ in range(min(len(heap), 10)):
            res.append(heappop(heap))
        return [tweet_id for _, tweet_id in res]

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followers[followerId]:
            self.followers[followerId].remove(followeeId)


def test():
    assert 2 + 2 == 4
