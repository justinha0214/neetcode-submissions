class Twitter:

    def __init__(self):
        self.users = defaultdict(list)
        self.feed = deque()

    def postTweet(self, userId: int, tweetId: int) -> None:
        tweet = [userId, tweetId]
        self.feed.appendleft(tweet)

    def getNewsFeed(self, userId: int) -> List[int]:
        count, res = 0, []
        for user, tweet in self.feed:
            if user == userId or user in self.users[userId]:
                res.append(tweet)
                count += 1
            if count == 10:
                break
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        if followeeId not in self.users[followerId]:
            self.users[followerId].append(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        if followeeId in self.users[followerId]:
            self.users[followerId].remove(followeeId)
