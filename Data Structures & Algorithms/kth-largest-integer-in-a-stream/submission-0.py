class KthLargest:
    #strream - we cna continuously add numbers to the list of numbers

    #so the easiest way of solving this is to sort the list of numbers
    #then take kth largest element... that can be done efficiently if oyu do binary search so run time O(log(N))
    #but to add an eleement in an array will be O(n)
    # so we go for min heap of size k 
    # cuz add/pop you can do in log (n) and 
    # if you find the minimum value you can do it in O(1)
    def __init__(self, k: int, nums: List[int]):
        self.minHeap, self.k = nums, k #self.minHeap is currently just an array now to turn it into a heap
        heapq.heapify(self.minHeap)  
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0] # return [0] cuz minimum value is always stored in the minimum index
        
