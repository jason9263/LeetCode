class TimeMap:

    def __init__(self):
        self.dic = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.dic:
            self.dic[key][0].append(timestamp)
            self.dic[key][1].append(value)
        else:
            self.dic[key] = [[timestamp], [value]]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dic:
            return ""
        times, values = self.dic[key]

        index = bisect.bisect_right(times, timestamp) - 1
        return values[index] if index >= 0 else ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
