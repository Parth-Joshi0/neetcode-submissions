class TimeMap:

    def __init__(self):
        self.storage = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        store = []
        if key in self.storage:
            store = self.storage[key]
        store.append((value, timestamp))
        self.storage[key] = store

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.storage:
            return ""

        store = self.storage[key]
        l, r = 0, len(store) - 1
        result = ""

        while l <= r:
            mid = l + (r-l)//2
            if store[mid][1] == timestamp:
                return store[mid][0]
            elif store[mid][1] > timestamp:
                r = mid - 1
            else:
                result = store[mid][0]
                l = mid + 1
        return result