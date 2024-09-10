class Solution:
    def lowestCommonAncestor(self, root, p, q):
        cur = root
        if p.val > q.val:
            p, q = q, p
        while True:
            if p.val <= cur.val <= q.val:
                return cur
            if cur.val > q.val:
                cur = cur.left
            else:
                cur = cur.right
