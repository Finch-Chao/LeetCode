class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        look = {}
        for i,num in enumerate(nums):
            if target - num in look:
                return [look[target - num],i]
            look[num] = i