class Solution(object):
    def longestCommonPrefix(self, strs):
        length = min(strs, key=len)
        ret = []
        for i in range(len(length)):
            dog = True
            check = list(strs[0])[i]
            for n in range(len(strs)):
                if(list(strs[n])[i]!=check):
                    dog = False
                    break
            if(dog):
                ret.append(check)
            else:
                break
        return "".join(ret)