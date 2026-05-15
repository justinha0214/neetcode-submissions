class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            num = len(s)
            newString = str(num) + "#" + s
            res += newString
        return res


    def decode(self, s: str) -> List[str]:
        ans = []
        pointer = 0
        while pointer < len(s):
            sLength = ""
            while s[pointer] != "#":
                sLength += s[pointer]
                pointer += 1
            sLength = int(sLength)
            pointer += 1
            newString = s[pointer:pointer+sLength]
            ans.append(newString)
            pointer += sLength
        return ans

        # Hello
        # 5#Hello5#World