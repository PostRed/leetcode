class Solution:
    def romanToInt(self, s: str) -> int:
        roman_numerals = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        total, prev_value = 0, 0
        for char in reversed(s):
            value = roman_numerals[char]
            # для значений типа 4 (IV)
            if value < prev_value:
                total -= value
            # а так - просто складываем
            else:
                total += value
            prev_value = value
        return total
