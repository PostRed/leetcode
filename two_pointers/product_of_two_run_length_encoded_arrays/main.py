class Solution:
    def findRLEArray(self, encoded1, encoded2):
        ans = []
        j = 0
        # значение, число повторений
        for val_i, freq_i in encoded1:
            while freq_i:
                # минимальное число повторений элемента
                freq_cur = min(freq_i, encoded2[j][1])
                val_cur = val_i * encoded2[j][0]

                if ans and ans[-1][0] == val_cur:
                    ans[-1][1] += freq_cur
                else:
                    ans.append([val_cur, freq_cur])

                freq_i -= freq_cur
                encoded2[j][1] -= freq_cur
                # если исчерпали повторы во втором списке - в нем переходи дальше
                if not encoded2[j][1]:
                    j += 1
        return ans
