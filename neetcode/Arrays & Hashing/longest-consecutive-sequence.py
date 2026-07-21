class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums = set(nums)
        nums = list(nums)
        nums.sort()
        best = 1
        cur = 0
        print(nums)
        for i in range(len(nums)):
            if nums[i]-1==nums[i-1] or cur==0:
                cur += 1
            elif cur>best:
                best = cur
                cur = 1
            else:
                cur = 1
            print(cur)
        if cur>best:
            best = cur
        return best