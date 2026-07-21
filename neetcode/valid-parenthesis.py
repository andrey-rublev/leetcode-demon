class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        temp = list(s)
        for i in temp:
            if i=="[" or i=="(" or i=="{":
                stack.append(i)
            else:
                if not stack:
                    return False
                x = stack.pop()
                if (i=="]" and x!="[") or (i=="}" and x!="{") or (i==")" and x!="("):
                    return False
        if stack:
            return False
        return True