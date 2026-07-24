class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ret1 = list(s)
        ret2 = list(t)
        ret1.sort()
        ret2.sort()
        if ret1 == ret2:
            return True
        return False