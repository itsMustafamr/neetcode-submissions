class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # way 1 - hashmap
        # if len(s) != len(t):
        #     return False
        
        # counts = {}
        # countt = {}
        # for i in range(len(s)):
        #     counts[s[i]] = 1 + counts.get(s[i], 0)
        #     countt[t[i]] = 1 + countt.get(t[i], 0)

        # for c in counts:
        #     if counts[c] != countt.get(c, 0):
        #         return False

        # return True
        # way 2
        # a = sorted(s)
        # b = sorted(t)

        # if a == b:
        #     return True
        # else:
        #     return False

        # way 3
        return Counter(s) == Counter(t)

                
        


        