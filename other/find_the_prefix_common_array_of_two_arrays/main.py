class Solution(object):
    def findThePrefixCommonArray(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        n = len(A)
        res = [0] * n
        count_A = set() 
        count_B = set()

        for i in range(n):
            count_A.add(A[i]) 
            count_B.add(B[i])

            # Количество общих элементов на индексе i
            res[i] = len(count_A.intersection(count_B))

        return res
