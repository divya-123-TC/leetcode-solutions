class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def dfs(root):
            if not root:
                return None
            lefttail=dfs(root.left)
            righttail=dfs(root.right)
            if root.left:
                lefttail.right=root.right
                root.right=root.left
                root.left=None
            last=righttail or lefttail or root
            return last
        dfs(root)