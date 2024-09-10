class Solution:
    def maxDepth(self, root):
        def dfs(node, size):
            if not node:
                return size
            return max(dfs(node.left, size), dfs(node.right, size)) + 1
        return dfs(root, 0)
        
