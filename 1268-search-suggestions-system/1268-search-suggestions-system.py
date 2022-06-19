class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        TR = lambda : defaultdict(TR)
        trie = TR()
        ITEMS = False
        for idx,product in enumerate(products):
            tmp = trie
            for c in product:
                tmp = tmp[c]
                if ITEMS not in tmp:
                    tmp[ITEMS] = []
                if len(tmp[ITEMS])<3:
                    tmp[ITEMS].append(idx)                    
        ans = []
        tmp = trie
        for w in searchWord:
            tempans = []
            tmp = tmp[w]
            if ITEMS in tmp:
                tempans.extend([products[i] for i in tmp[ITEMS]])
            ans.append(list(tempans))
        return ans