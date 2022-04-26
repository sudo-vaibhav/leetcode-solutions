class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        def func(item):
            typ,col,nam = item
            return (ruleKey == "type" and ruleValue == typ) or (ruleKey == "color" and ruleValue == col) or (ruleKey == "name" and ruleValue == nam)
            
        return len(list(filter(func,items)))