class Solution:
    def camelMatch(self, qs: List[str], p: str) -> List[bool]:
        def upper(q):
            return [c for c in q if c.isupper()]
        ans = []
        for q in qs:
            it = iter(q)
            ans.append(upper(q)==upper(p) and all(c in it for c in p))
        return ans
        # def u(s):
        #     return [c for c in s if c.isupper()]

#         def issup(s, t):
#             it = iter(t)
#             return all(c in it for c in s)

        # return [upper(p) == upper(q) and issup(p, q) for q in qs]