class TimeMap:
    def __init__(self):
        pass
    
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.time_map:
            self.time_map[key] = []

    def get(self, key: str, timestamp: int) -> str:
        pass


obj = TimeMap()
obj.set(key, value, timestamp)
param_2 = obj.get(key,timestamp)
