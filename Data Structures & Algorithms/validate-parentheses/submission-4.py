class Solution:
    def isValid(self, s: str) -> bool:
        hashMap = {
            "}" : "{",
            "]" : "[",
            ")" : "("
        }
        stack = []
        for c in s:
            if c not in hashMap:
                stack.append(c)
            else:
                if stack and stack[-1] == hashMap[c]:
                    stack.pop()
                else: 
                    return False
        return True if not stack else False