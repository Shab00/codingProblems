class TimeMap:
    def __init__(self):
        self.time_map = {}
    
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.time_map:
            self.time_map[key] = []
        self.time_map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.time_map:
            return ""
        pairs = self.time_map[key]
        left, right = 0, len(pairs) - 1
        res = ""
        while left <= right:
            mid = (left + right) // 2
            mid_timestamp, mid_value = pairs[mid]
            if mid_timestamp <= timestamp:
                res = mid_value 
                left = mid + 1
            else:
                right = mid - 1
        return res



key = "foo"
value = "bar"
timestamp = 1
obj = TimeMap()
obj.set(key, value, timestamp)
param_2 = obj.get(key,timestamp)
