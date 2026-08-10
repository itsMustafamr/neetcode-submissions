class Solution:
    def isValid(self, s: str) -> bool:
        #brutforce
        # while '()' in s or '{}' in s or '[]' in s:
        #     s = s.replace('()','')
        #     s = s.replace('{}','')
        #     s = s.replace('[]','')
        # return s == ''

        #way 2 - stack and hashmap
        stack = []
        mapper = {")" : "(", "]" : "[", "}" : "{"}

        for i in s:
            if i in mapper:
                if stack and stack[-1] == mapper[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)        

        return True if not stack else False #return true if stack empty else false.








        