class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []
        for i in range(len(temperatures)):
            j = temperatures[i]
            print(stack)
            while stack:
                if temperatures[stack[-1]]>=j:
                    break
                x = stack.pop()
                result[x] = i-x
            stack.append(i)
        return result