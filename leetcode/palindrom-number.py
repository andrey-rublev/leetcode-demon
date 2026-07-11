class Solution(object):
    def isPalindrome(self, x):
        nums = list(str(x))
        for i in range(len(nums)):
            if(nums[i]!=nums[len(nums)-i-1]):
                return False
        return True