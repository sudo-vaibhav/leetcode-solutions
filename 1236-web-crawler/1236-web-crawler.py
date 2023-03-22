# """
# This is HtmlParser's API interface.
# You should not implement it, or speculate about its implementation
# """
#class HtmlParser(object):
#    def getUrls(self, url):
#        """
#        :type url: str
#        :rtype List[str]
#        """

class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        ans = set()
        def getBase(url):
            return url.split("/")[2]
        BASE = getBase(startUrl)
        def solve(url):
            if getBase(url)==BASE and url not in ans:
                ans.add(url)
                urls = htmlParser.getUrls(url)
                for url in urls:
                    solve(url)
        solve(startUrl)
        
        return list(ans)