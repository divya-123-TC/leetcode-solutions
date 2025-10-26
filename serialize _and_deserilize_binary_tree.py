class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def doit(node):
            if node:
                vals.append(str(node.val))
                doit(node.left)
                doit(node.right)
            else:
                vals.append('#')
        vals=[]
        doit(root)
        return " ".join(vals)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def doit():
            val=next(vals)
            if val=="#":
                return None
            node=TreeNode(int(val))
            node.left=doit()
            node.right=doit()
            return node
        vals=iter(data.split())
        return doit()        
