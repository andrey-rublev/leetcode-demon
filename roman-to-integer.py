class Solution(object):
    def romanToInt(self, s):
        letters = list(s)
        nums = []
        for i in letters:
            if(i=="I"):
                nums.append(1)
            elif(i=="V"):
                nums.append(5)
            elif(i=="X"):
                nums.append(10)
            elif(i=="L"):
                nums.append(50)
            elif(i=="C"):
                nums.append(100)
            elif(i=="D"):
                nums.append(500)
            elif(i=="M"):
                nums.append(1000)
        sum = 0
        for i in range(len(nums)):
            if(i!=len(nums)-1 and nums[i]<nums[i+1]):
                sum+=nums[i]*-1
            else:
                sum+=nums[i]
        return sum