class Solution:
    def isPalindrome(self, s: str) -> bool:
        temp = s.split(" ")
        s = "".join(temp)
        temp = list(s.lower())
        x = 0
        for i in range(len(temp)):
            j = ord(temp[i-x])
            if j<48 or (j>57 and j<65) or (j>90 and j<97) or j>122:
                temp.pop(i-x)
                x += 1
        j = len(temp)-1
        for i in temp:
            if i!=temp[j]:
                return False
            j = j - 1
        return True