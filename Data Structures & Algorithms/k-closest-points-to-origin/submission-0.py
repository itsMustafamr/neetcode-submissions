class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #HERE a^2 + b^2 = c^2
        # and we are tryinh to ffind the c here that is the shortest distance or the displacement
        # we find c then sort it that gives the time complexity = nlogn
        #but we only need for k  closest point so we go with min heap

        #here we apply heapify algorithm after we find the distane and put it in the form [distance, (x-x_1)^2 , (y-y_1)^2] so O(n) only here..
        # overall k(logn)

        minHeap = []
        for x, y in points:
            dist = (x ** 2) + (y ** 2)
            minHeap.append([dist, x, y])

        heapq.heapify(minHeap)
        res = []
        while k > 0:
            dist, x, y = heapq.heappop(minHeap)
            res.append([x, y])
            k -= 1 
            
        return res
