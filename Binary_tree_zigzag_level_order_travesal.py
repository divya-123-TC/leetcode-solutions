class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res=[]
        if not root:
            return res
        q=collections.deque()
        q.append(root)
        left_to_right=True
        while q:
            same_level=[]
            for _ in range(len(q)):
                node=q.popleft()
                same_level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if not left_to_right:
                same_level.reverse()
            res.append(same_level)
            left_to_right=not left_to_right
        return res