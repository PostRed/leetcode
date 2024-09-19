class Solution(object):
    def subarraysDivByK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        pref = [0] * (len(nums) + 1)
        rem = [0] * k

        for i in range(len(nums)):
            pref[i + 1] = pref[i] + nums[i]
            rem[pref[i + 1] % k] += 1

        ans = (rem[0] * (rem[0] + 1)) // 2
        for i in range(1, k):
            ans += (rem[i] * (rem[i] - 1)) // 2
        return ans
