from sortedcontainers import SortedSet
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        TR = lambda : defaultdict(TR)
        trie = TR()
        ITEMS = "items"
        for product in products:
            tmp = trie
            for c in product:
                tmp = tmp[c]
                if ITEMS not in tmp:
                    tmp[ITEMS] = SortedSet()
                tmp[ITEMS].add(product)
                if len(tmp[ITEMS])>3:
                    tmp[ITEMS].pop()
        ans = []
        tmp = trie
        for w in searchWord:
            tempans = []
            tmp = tmp[w]
            if ITEMS in tmp:
                tempans.extend(tmp[ITEMS])
            ans.append(list(tempans))
        return ans