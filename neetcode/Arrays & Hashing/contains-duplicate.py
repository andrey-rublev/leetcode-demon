class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        ret = set(nums)
        if len(ret) == len(nums):
            return False
        return True