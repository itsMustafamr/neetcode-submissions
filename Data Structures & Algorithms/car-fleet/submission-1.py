class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # pair = [[p, s] for p, s in zip(position, speed)] # or use hashmap

        # stack = [] # we sort the pair based on position
        # for p, s in sorted(pair)[::-1]:#reverse sorted order or we go from right to left cuz we want to see the end car collition with rest of them
        #     stack.append((target - p) / s) # target - position / speed -> car fleet
        #     if len(stack) >= 2 and stack[-1] <= stack [-2]:
        #         stack.pop()
        # return len(stack)   #so basically if the time is smaller than the car ahead then they are gonna collide (basically car fleet happens)

        pair = [[p, s] for p, s in zip(position, speed)]

         
        stack = []
        pair.sort(reverse = True)

        for p, s in pair:
            stack.append((target - p) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]: #not using while cuz we already start checking from back so it will already be covered
                stack.pop()
            
        return len(stack)





            


         
        