class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        retDict = Counter(nums)
        keys = list(retDict.keys())
        values = list(retDict.values())
        retList = []
        while values:
            big = max(values)
            num = keys.pop(values.index(big))
            values.remove(big)
            retList.append(num)
        return retList[0:k]