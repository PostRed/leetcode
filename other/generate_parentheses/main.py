class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        #  Правильные скобки должны удовлетворять двум условиям:
        #    - Количество ( не должно превышать n.
        #    - Количество ) не должно превышать количества открывающих скобок в данный момент.
        stack, res = [], []
        def recursion(open, close):
            if open == close and open == n:
                res.append(''.join(stack))
                # стек вызова идет снизу вверх
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

print(Solution().generateParenthesis(3))
