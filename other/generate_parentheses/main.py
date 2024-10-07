class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        stack, res = [], []
        def recursion(open, close):
            print(open, close)
            if open == close and open == n:
                res.append(''.join(stack))
                return
            if open < n:
                stack.append('(')
                recursion(open + 1, close)
                stack.pop()
            if close < open:

                stack.append(')')
                recursion(open, close + 1)
                stack.pop()

        recursion(0, 0)
        return res
