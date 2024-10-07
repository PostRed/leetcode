class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        # Записываем еще числа, которые начинаются на 4 и 9, так они состоят из 2х символов
        val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
        ]
        syms = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
        ]
        res = ''
        i = 0
        while num > 0:
            for _ in range(num // val[i]):
                res += syms[i]
                num -= val[i]
            i += 1
        return res
