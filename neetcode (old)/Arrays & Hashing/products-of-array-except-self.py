class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total = 1
        zero = 0
        for i in nums:
            if i!=0:
                total = total * i
            else:
                zero = zero + 1
        ret = list()
        if zero>1:
            return [0] * len(nums)
        if zero==0:
            for j in range(len(nums)):
                ret.append(int(total/nums[j]))
        else:
            for j in range(len(nums)):
                if nums[j]!=0:
                    ret.append(0)
                else:
                    ret.append(total)
        return ret