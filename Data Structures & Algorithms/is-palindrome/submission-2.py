class Solution:
    def isPalindrome(self, s: str) -> bool:
        # way 3
        # newStr = ""

        # for c in s:
        #     if c.isalnum():
        #         newStr += c.lower()
        # return newStr == newStr[::-1]
        # way 1
        # filtered = ''.join(c.lower() for c in s if c.isalnum())
        # return filtered == filtered[::-1]
        # way 2 
        # L = 0
        # R = len(s) - 1

        # while L < R:
        #     while L < R and not s[L].isalnum():
        #         L += 1
        #     while L < R and not s[R].isalnum():
        #         R -= 1
            
        #     if s[L].lower() != s[R].lower():
        #         return False
            
        #     L += 1
        #     R -= 1

        # return True 
        # easy method
        # sr = ""
        # for i in s:
        #     if i.isalnum():
        #         sr = sr + i.lower()
        # return sr == sr[::-1]
        #two pointer method
        l = 0 
        r = len(s) - 1

        while l < r:
            while l < r and not self.isalnum(s[l]):
                l += 1
            while l < r and not self.isalnum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l, r = l + 1, r - 1
        return True

    def isalnum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))

