class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = deque()
        for ast in asteroids:
            if len(stack)==0 or ast>0:
                stack.append(ast)
            else:
                while stack and stack[-1]>0 and stack[-1]<-ast:
                    stack.pop()
                if stack and stack[-1]==-ast:
                    stack.pop()
                elif len(stack)==0 or stack[-1]<0:
                    stack.append(ast)
        return stack