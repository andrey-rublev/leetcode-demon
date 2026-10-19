class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        one = list(s)
        one.sort()
        two = list(t)
        two.sort()
        if one == two:
            return True
        return False