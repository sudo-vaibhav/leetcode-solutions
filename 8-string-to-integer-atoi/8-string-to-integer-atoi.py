start,processing,end = 0,1,2
class Solution:
    def myAtoi(self, s: str) -> int:
        class Automaton:
            def __init__(self):
                self.state = start
                self.mult = 1
                self.val = 0
            
            def process(self,c):
                if self.state==start:
#                   keep ignoring whitespaces
                    if c==" ":
                        return
                    else:
                        self.state = processing # start phase over
                        if c=="+" or c=="-":
                            if c=="-":
                                self.mult=-1    
                        else:
#                           nums should start now, so process it again to count that num without writing
#                           more logic in start phase
                            self.process(c)
                elif self.state==processing:
                    if c.isdigit():
                        temp = self.val*10+int(c)
                        self.val = min(2**31,temp) # since values can only be positive, sign will be added later
                    else:
                        self.state=end
                        
            def verdict(self):
                base = self.val
                if base == 2**31 and self.mult==1:
                    base-=1 # negatives go till 2**31 abs value, but positive only till 2**31 - 1
                return self.mult*base
    
        automaton = Automaton()
        
        for c in s:
            automaton.process(c)
        
        return automaton.verdict()