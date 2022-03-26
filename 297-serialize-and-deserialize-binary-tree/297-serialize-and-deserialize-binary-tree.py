# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        if not root: return ""
        
        lot = []
        q = deque()
        q.append(root)
        
        while q:
            node = q.popleft()
            if not node:
                lot.append("#")
            else:
                lot.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
        # print(lot)
        return " ".join(lot)

    def deserialize(self, data):
        if data=="": return
        nodes = data.split(" ")
        t=1
        q = deque()
        root = TreeNode(int(nodes[0]))
        q.append(root)
        while q:
            cur = q.popleft()
            l = nodes[t]
            r = nodes[t+1]
            if(l=="#"):
                pass
            else:
                cur.left = TreeNode(int(l))
                q.append(cur.left)
            if(r=="#"):
                pass
            else:
                cur.right = TreeNode(int(r))
                q.append(cur.right)
            t+=2
            
        return root
                
            

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))