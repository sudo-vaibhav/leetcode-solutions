class Twitter:

    def __init__(self):
        # self.tweets = []
        self.time = 0
        self.following = defaultdict(set)
        self.tweetHeads = defaultdict(lambda : None)

    def postTweet(self, userId: int, tweetId: int) -> None:
        tweet = (-self.time,tweetId,self.tweetHeads[userId])
        self.tweetHeads[userId] = tweet
        self.time+=1


    def getNewsFeed(self, userId: int) -> List[int]:
        # n = len(self.tweets)
        ans = []
        
        heads = []
        for followedUser in [*self.following[userId],userId]:
            if self.tweetHeads[followedUser]!=None:
                heappush(heads,self.tweetHeads[followedUser])
        
        while heads and len(ans)<10:
            cur = heappop(heads)
            nex = cur[2]
            ans.append(cur[1])
            if nex!=None:
                heappush(heads,nex)
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