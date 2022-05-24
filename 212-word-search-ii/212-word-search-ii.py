class TrieNode():
    def __init__(self):
        self.children = [None for _ in range(26)]
        self.word = None
        
class Solution:
    moves = [[0,1],[0,-1],[1,0],[-1,0]]
    def buildTrie(self,words):
        root = TrieNode()
        a = ord("a")
        for word in words:
            node = root
            for char in word:
                c = ord(char)
                if node.children[c-a] == None:
                    node.children[c-a] = TrieNode()
                node = node.children[c-a]
            node.word = word
        return root
        
    def dfs(self,board,i,j,node):
        c = board[i][j]
        A = ord("a")
        C = ord(c)
        orig = node
        node = node.children[C-A]
        if node==None: return
        if node.word!=None:
            self.ans.append(node.word)
            node.word = None # de-duplicate
            if node.children.count(None)==26:
                orig.children[C-A] = None
        board[i][j] = "#"
        for di,dj in self.moves:
            I,J = i+di,j+dj
            if 0<=I<self.m and 0<=J<self.n and board[I][J]!="#":
                self.dfs(board,I,J,node)
        board[i][j] = c
            
        
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.m,self.n = len(board),len(board[0])
        root = self.buildTrie(words)  
        self.ans = []
        for i in range(self.m):
            for j in range(self.n):
                self.dfs(board,i,j,root)
        
        return self.ans