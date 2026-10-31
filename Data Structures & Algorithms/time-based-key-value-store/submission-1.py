class TimeMap:

    def __init__(self):
        self.time_map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if self.time_map.get(key):
            self.time_map[key].append([timestamp, value])
        else:
            self.time_map[key] = [[timestamp, value]]
        
    def get(self, key: str, timestamp: int) -> str:
        if key in self.time_map:
            timestamp_vals = self.time_map[key]
            #Do BS on timestamps , if not found then used latest value 
            l, r = 0 , len(timestamp_vals)-1
            res = ""

            while l <= r:
                mid = l + (r-l)//2
                if timestamp_vals[mid][0] <= timestamp:
                    res = timestamp_vals[mid][-1]
                    l = mid + 1
                else:
                    r = mid - 1
            
            return res
        
        return ""