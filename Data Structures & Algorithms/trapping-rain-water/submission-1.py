class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        # we take min of 2 block that is the bottleneck, that gives how much water we can trap.
        #so for between the blocks we do min (L, R) - h[i]
        # way 1 - brutforce
        # if not height:
        #     return 0
        # n = len(height)
        # res = 0

        # for i in range(n):
        #     leftMax = rightMax = height[i]

        #     for j in range(i):
        #         leftMax = max(leftMax, height[j])
        #     for j in range(i + 1, n):
        #         rightMax = max(rightMax, height[j])
                
        #     res += min(leftMax, rightMax) - height[i]
        # return res
        # #way 2-  2 pointer way
        # if not height:
        #     return 0

        # l, r = 0, len(height) - 1
        # lmax, rmax = height[l], height[r]
        # res = 0

        # while l < r:
        #     if lmax < rmax:
        #         l += 1
        #         lmax = max(lmax, height[l]) 
        #         res += lmax - height[l]
        #     else:
        #         r -= 1
        #         rmax = max(rmax, height[r])
        #         res += rmax - height[r]

        # return res
                

                # min(l , r) 
                # water = max(height[l], height[r]) - height[i]

                # min(res, total(max(l, r)))


                # water trap = min (max(height[l], height[r])) - height[i]
        
        if not height:
            return 0
        l = 0
        r = len(height) - 1
        res = 0
        lmax, rmax = height[l], height[r]

        while l < r:
            if lmax < rmax:
                l += 1
                lmax = max(lmax, height[l])
                res += lmax - height[l]

            else:
                r -= 1
                rmax = max(rmax, height[r])
                res += rmax - height[r]

        return res


            
