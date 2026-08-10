class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #way 1 - stack
        #montonic decreasing order
        stack = [] # pair : [temp, index]
        res = [0] * len(temperatures)
        
        for i,t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()
                res[stackInd] = (i - stackInd)
            stack.append([t, i])
        return res
        #way 2 - brutforce
        # n = len(temperatures)
        # res = []

        # for i in range(n):
        #     count = 1
        #     j = i + 1
        #     while j < n:
        #         if temperatures[j] > temperatures[i]:
        #             break
        #         j += 1
        #         count += 1
        #     count = 0 if j == n else count
        #     res.append(count)
        # return res