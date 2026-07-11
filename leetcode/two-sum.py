class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for n in range(len(nums)):
                if(i!=n and nums[i]+nums[n]==target):
                    return [i,n]