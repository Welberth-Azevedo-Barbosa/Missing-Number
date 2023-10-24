class Solution(object):
    def missingNumber(self, nums):
        result = 0
        for counter, value in enumerate(nums):
            result ^= counter+1
            result ^= value
        return result
