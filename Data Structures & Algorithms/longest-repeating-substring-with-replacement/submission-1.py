class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
    # will be solved in O(26.n)
    #brut force ( we use a hashmap count to get the count of most frequent charecter )
        # res = 0
        # for i in range(len(s)):
        #     count, maxf = {},0
        #     for j in range(i, len(s)):
        #         count[s[j]] = 1 + count.get(s[j], 0)
        #         maxf = max(maxf, count[s[j]])
        #         if ( j - i + 1 ) - maxf <= k :
        #             res = max(res, j - i + 1)
        # return res
    #best solution
        # l = 0
        # #when l - (count of the most fequent charecter) = value <= k then it is valid then we update res
        # count = {}
        # res = 0

        # for r in range(len(s)):
        #     count[s[r]] = 1 + count.get(s[r], 0)
            
        #     while (r - l + 1) - max(count.values()) > k:
        #         count[s[l]] -= 1 
        #         l += 1

        #     res = max(res, r - l + 1)
        # return res
        l = 0
        res = 0
        count = {}

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            
            while (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)
        return res
