class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dct = {}
        for el in strs:
            k = ''.join(sorted(list(el)))
            if k in dct:
                dct[k].append(el)
            else:
                dct[k] = [el]
        return list(dct.values())
