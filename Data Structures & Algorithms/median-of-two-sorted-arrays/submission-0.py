class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        #way 1 - worst way - (m+n)log(m+n)
        # merged = sorted(nums1 + nums2)  # just merge + sort
        # n = len(merged)
        # if n % 2 == 0:
        #     return (merged[n//2 - 1] + merged[n//2]) / 2
        # else:
        #     return merged[n//2]
            
        #way 2 - O(m+n)
        #Merge both arrays like merge-sort
        #Find median from merged list

        # merged = []
        # i = j = 0

        # # Merge the two arrays using two pointers
        # while i < len(nums1) and j < len(nums2):
        #     if nums1[i] < nums2[j]:
        #         merged.append(nums1[i])
        #         i += 1
        #     else:
        #         merged.append(nums2[j])
        #         j += 1

        # # Append remaining elements
        # while i < len(nums1):
        #     merged.append(nums1[i])
        #     i += 1
        # while j < len(nums2):
        #     merged.append(nums2[j])
        #     j += 1

        # n = len(merged)
        # if n % 2 == 0:
        #     return (merged[n // 2] + merged[n // 2 - 1]) / 2
        # else:
        #     return merged[n // 2]



        #way 3 - best - O(long(m+n))
        A, B = nums1, nums2 
        total = len(nums1) + len(nums2)
        half = total // 2 #integer division so we use // 

        if len(B) < len(A):
            A, B = B, A

        l, r = 0, len(A) - 1
        while True:
            i = (l + r) // 2 # this is the pointer for A
            j = half - i - 2 # j is the index of mid point, -2 cuz j starts at 0 and i starts at 0

            Aleft = A[i] if i >= 0 else float("-infinity")
            Aright = A[i + 1] if (i + 1) < len(A) else float("infinity")
            Bleft = B[j] if j >= 0 else float("-infinity")
            Bright = B[j + 1] if (j + 1) < len(B) else float("infinity")

            #partition is correct
            if Aleft <= Bright and Bleft <= Aright:
                # odd
                if total % 2:
                    return min(Aright, Bright)
                # even
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1

        



