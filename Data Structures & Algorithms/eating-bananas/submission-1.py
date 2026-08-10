class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #way 1 - brutforce - O(max(pile) * pile) - O(m * n)
        # speed = 1
        # while True:
        #     totalTime = 0
        #     for pile in piles:
        #         totalTime += math.ceil(pile / speed)
            
        #     if totalTime <= h:
        #         return speed
        #     speed += 1    
        # return speed
        #way 2 - binary search - O(log m * n) - O(n log m)
        # l, r = 1, max(piles)
        # res = r # only cuz we are looking for minimum so we didn't initialize to 0 
        # # r which is the max of the pile

        # while l <= r:
        #     k = (l + r) // 2
        #     hours = 0
        #     for p in piles:
        #         hours += math.ceil(p / k)

        #     if hours <= h:
        #         res = min(res, k)
        #         r = k - 1
            
        #     else:
        #         l = k + 1
            
        # return res
        # l = 0
        # r = len(piles)

        # while r <= h:
        
        l = 1
        r = max(piles)

        res = r

        while l <= r:
            k = (l + r)// 2
            hours = 0

            for x in piles:
                hours += math.ceil(x / k)

            if  hours <= h:
                res = min(res, k)
                r = k - 1
            else:
                l = k + 1

        return res
    
