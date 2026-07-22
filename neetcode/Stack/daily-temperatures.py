class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = []
        for i in range(len(temperatures)):
            big = False
            j = i+1
            while big==False and j<len(temperatures):
                if temperatures[j]>temperatures[i]:
                    big = True
                j+=1
            if big == False:
                result.append(0)
            else:
                result.append(j-1-i)
        return result