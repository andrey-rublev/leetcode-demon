class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ret = []
        i = 0
        while i < len(strs):
            tempList = [strs[i]]
            j = i + 1
            while j < len(strs):
                if sorted(list(strs[i]))==sorted(list(strs[j])):
                    tempList.append(strs[j])
                    strs.pop(j)
                    j = j - 1
                j = j + 1
            ret.append(tempList)
            i = i + 1
        return ret