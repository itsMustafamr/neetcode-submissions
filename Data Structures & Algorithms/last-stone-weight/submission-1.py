class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # always take the 2 heviest stone
        # so easy way sort it...
        # but then we can do better is to use heap
        # but max heap..
        # python doesnt have a max heap fn so we have to use a minheap to simulate a max heap
        #so we do multiply every value by -1 to get it...

        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            if second > first: # we are taking second < first but we are doing -ve for all initially so we did multipleid -ve value
                heapq.heappush(stones, first - second) # or second - first * -1
        stones.append(0)
        return abs(stones[0])# so if there is already a stone in this list then it will return that index or it will add this 0 stone and end of reutrning this 0 instead





        