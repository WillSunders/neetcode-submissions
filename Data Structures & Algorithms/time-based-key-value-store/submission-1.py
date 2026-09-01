class TimeMap:

    def __init__(self):
        self.vals = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.vals:
            self.vals[key].append([value, timestamp])
        else:
            self.vals[key] = [[value, timestamp]]
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.vals:
            return ""
        val = self.vals.get(key)
        left = 0
        right = len(val) - 1
        result = ""
        while left <= right:
            mid = left + (right - left) // 2
            if val[mid][1] <= timestamp:
                result = val[mid][0]
                left = mid + 1
            else:
                right = mid - 1
        return result

