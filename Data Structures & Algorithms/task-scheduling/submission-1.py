class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

       #best way is to start with the most frequent element then process it (pretty much reduces the ideal time..by filling up)
# for this we can use maxheap
        #we add the processed things to the queue... after poping at each point
        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()] #this is actually minheap if we heapify it - cuz pyhton doesnt have maxheap direct function
        heapq.heapify(maxHeap)
        
        time = 0
        q = deque() # we initialize a queue - pair of [-cnt, idleTime]
        #also this queue is a double ended queue to keep track of time too

        while maxHeap or q:
            time += 1
            if maxHeap:
                cnt =  1 + heapq.heappop(maxHeap) #cuz in our case we have the cnt current fully in -ve so we have to add to make it bigger value or to null
                if cnt:
                    q.append([cnt, time + n])

            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
                #cuz only care about first value cnt ie

        return time

