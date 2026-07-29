class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lend = 0
        rend = len(nums)-1
        mid = 0
        while lend<=rend:
            mid = (lend+rend)//2
            if nums[mid]>target:
                rend = mid - 1
            elif nums[mid]<target:
                lend = mid + 1
            else:
                return mid
        if nums[mid]==target:
            return mid
        return -1