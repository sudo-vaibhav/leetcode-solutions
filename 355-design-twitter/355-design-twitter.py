class Twitter:

    def __init__(self):
        self.tweets = []
        self.following = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets.append({
            "userId":userId,"tweetId":tweetId
        })

    def getNewsFeed(self, userId: int) -> List[int]:
        n = len(self.tweets)
        ans = []
        for i in range(n-1,-1,-1):
            cur = self.tweets[i]
            if cur["userId"] == userId or cur["userId"] in self.following[userId]:
                ans.append(cur["tweetId"])
            if len(ans)==10:
                break
        return ans
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)