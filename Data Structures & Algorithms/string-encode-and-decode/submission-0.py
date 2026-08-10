class Solution:

    def encode(self, strs: List[str]) -> str:
        # 4#_ _ _ _ 5#_ _ _ _ _
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = [] #result will be a list of string
        i = 0 

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j]) #converts string to int
            res.append(s[j + 1 : j + 1 + length])
            i = j + 1 + length
        return res
