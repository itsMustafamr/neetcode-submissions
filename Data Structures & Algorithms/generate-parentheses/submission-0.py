class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # )( this is invalid 
        # for n = 3, 3 open, 3 close
        # close < open
        # only add open parenthesis if open < n
        # only add closing parenthesis if close < open
        # valid if and only if open == closed == n

        res = []
        stack = []

        def backtrack(openPar, closePar):
            if closePar == openPar == n:
                res.append("".join(stack))
                return
            
            if openPar < n:
                stack.append("(")
                backtrack(openPar + 1, closePar)
                stack.pop()

            if closePar < openPar:
                stack.append(")")
                backtrack(openPar, closePar + 1)
                stack.pop()
            
        backtrack(0,0)
        return res


        