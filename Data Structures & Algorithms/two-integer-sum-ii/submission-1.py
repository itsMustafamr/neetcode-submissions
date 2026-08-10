#so here if we do brut force. every number is compared to the next number
# then we can do 1st element to 2nd element then 1st element to 3rd element
# this works but bad and long
# so 2 pointer
# 1 at the beginning and one at the end
# end number if its bigger than target that is risgarded then we shift the pointer 
# to left. then we recompute it by shifting to right


#Non-decreasing order:
#Elements can stay the same or increase.

#increasing order:
#Elements must strictly increase.

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #way 1 - brut force - o(n^2)
        # for i in range(len(numbers)):
        #     for j in range(i + 1 , len(numbers)):
        #         if numbers[i] + numbers[j] == target:
        #             return [i + 1,j + 1]
        # #way 2 - two pointer - best 
        # l = 0
        # r = len(numbers) - 1

        # while l < r:
        #     curSum = numbers[l] + numbers[r]
        #     if curSum > target:
        #         r = r - 1
        #     if curSum < target:
        #         l = l + 1
        #     if curSum == target: # or else:
        #         return [l + 1, r + 1]
        # return []
        

        l = 0
        r = len(numbers) - 1        

        while l < r:
            cur = numbers[l] + numbers[r]
            if cur > target:
                r -= 1
            if cur < target:
                l += 1
            if cur == target:
                return [l + 1, r + 1]        
        
        return []





                


                
