class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # way 1 - best
        # count = {}
        # # index = freqency of that element, values = list of values that occur that particular many times
        # freq = [[] for i in range(len(nums) + 1)] #[[] - is an empty array in this case]

        # for n in nums:
        #     count[n] = 1 + count.get(n, 0)
        # for n, c in count.items():
        #     freq[c].append(n)

        # res = []
        # for i in range(len(freq) - 1, 0, -1):
        #     for n in freq[i]:
        #         res.append(n)
        #         if len(res) == k:
        #             return res 

# runtime - O(n)
        # way 2
        # count = Counter(nums)
        # most_frequent = [item for item, freq in count.most_common(k)]
        # return most_frequent

        # way 3
        # frequency_dict = {}
        # for num in nums:
        #     if num in frequency_dict:
        #         frequency_dict[num] += 1
        #     else:
        #         frequency_dict[num] = 1

        # sorted_elements = sorted(frequency_dict.items(), key=lambda x: x[1], reverse=True)
        # top_k_frequent = [item for item, freq in sorted_elements[:k]]
        # return top_k_frequent

        # way 4 - heapify
        frequency_dict = {}
        for num in nums:
            if num in frequency_dict:
                frequency_dict[num] += 1
            else:
                frequency_dict[num] = 1
        
        heap = []
        
        for num, freq in frequency_dict.items():
            heapq.heappush(heap, (freq, num))
            
            if len(heap) > k:
                heapq.heappop(heap)
        
        top_k_frequent = [num for freq, num in heap]
        
        return top_k_frequent




                
