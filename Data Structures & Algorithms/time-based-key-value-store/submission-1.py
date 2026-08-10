class TimeMap:

    def __init__(self):
        # self.store = {}  # key -> list of [value, timestamp]
        self.store = {}



    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([value, timestamp])
        # if key in self.store:
        #     self.store[key] = []
        
        # self.store[key].append([value, timestamp])  
 




    def get(self, key: str, timestamp: int) -> str:
        # res = ""
        # values = self.store.get(key, [])  # get list of [val, ts] for the key

        # # binary search for the latest ts <= given timestamp
        # l, r = 0, len(values) - 1
        # while l <= r:
        #     m = (l + r) // 2
        #     if values[m][1] <= timestamp:
        #         res = values[m][0]  # store candidate result
        #         l = m + 1           # try to find a closer one
        #     else:
        #         r = m - 1
        # return res

        res = ""
        value = self.store.get(key, [])

        l, r = 0, len(value) - 1
        while l <= r:
            m = (l + r)// 2
            if value[m][1] <= timestamp:
                res = value[m][0]
                l = m + 1
            else:
                r = m - 1
        
        return res




