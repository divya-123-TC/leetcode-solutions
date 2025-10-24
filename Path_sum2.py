class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res=[]
        def dfs(node,path,curr_sum):
            if not node:
                return
            path.append(node.val)
            curr_sum+=node.val
            if not node.left and not node.right and curr_sum==targetSum:
                res.append(list(path))
            dfs(node.left,path,curr_sum)
            dfs(node.right,path,curr_sum)
            path.pop()
        dfs(root,[],0)
        return res