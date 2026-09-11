class TimeMap:

    def __init__(self):
        self.kvstore = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.kvstore:
            self.kvstore[key] = []
        self.kvstore[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res, vals = "", self.kvstore.get(key, [])
        left, right = 0, len(vals) - 1
        while left <= right:
            mid = (left + right) // 2
            if vals[mid][1] <= timestamp:
                res = vals[mid][0]
                left = mid + 1
            else:
                right = mid - 1
        return res