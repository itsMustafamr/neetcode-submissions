class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # way 1
#         # a set of words is an anagram if we sort each of them then
#         # both of the words will be the equal
#         # count [a - z] = 1e, 1a, 1t -> we use hashmap to count the
#         # number of charecters
#         #res = {} - instad of empty hashmap we use a defaultdict
#         res = defaultdict(list)

#         for i in strs:
#             count = [0] * 26 # ie a ....z -> so 26 zeros ....

#             for c in i:
#                 count[ord(c) - ord("a")] += 1
#             res[tuple(count)].append(i)

#         return list(res.values())

# # runtime - O(m * n)
        # way 2
        count = defaultdict(list)
        for i in strs:
            sortedi = ''.join(sorted(i))
            count[sortedi].append(i)
        return list(count.values())
# runtime - O(m * n * logn)
         