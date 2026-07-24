class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        freq = Counter(numbers)
        for i in range(len(numbers)):
            opp = target - numbers[i]
            if list(freq.values())[opp]>0 and numbers[i]!=opp:
                return [target-opp, opp]
            