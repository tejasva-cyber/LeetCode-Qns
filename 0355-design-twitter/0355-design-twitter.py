import heapq

class Twitter:

    def __init__(self):
        self.time = 0
        self.tweets = {}
        self.following = {}

    def postTweet(self, userId, tweetId):
        if userId not in self.tweets:
            self.tweets[userId] = []

        self.time += 1
        self.tweets[userId].append((self.time, tweetId))

    def getNewsFeed(self, userId):
        users = self.following.get(userId, set()) | {userId}

        heap = []

        for user in users:
            if user in self.tweets and self.tweets[user]:
                index = len(self.tweets[user]) - 1
                time, tweetId = self.tweets[user][index]
                heapq.heappush(heap, (-time, tweetId, user, index))

        result = []

        while heap and len(result) < 10:
            _, tweetId, user, index = heapq.heappop(heap)
            result.append(tweetId)

            if index > 0:
                index -= 1
                time, tweetId = self.tweets[user][index]
                heapq.heappush(
                    heap,
                    (-time, tweetId, user, index)
                )

        return result

    def follow(self, followerId, followeeId):
        if followerId == followeeId:
            return

        if followerId not in self.following:
            self.following[followerId] = set()

        self.following[followerId].add(followeeId)

    def unfollow(self, followerId, followeeId):
        if followerId in self.following:
            self.following[followerId].discard(followeeId)