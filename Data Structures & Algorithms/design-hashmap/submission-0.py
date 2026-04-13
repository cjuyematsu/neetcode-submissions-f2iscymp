class MyHashMap:

    def __init__(self):
        self.keys = []
        self.vals = []

    def put(self, key: int, value: int) -> None:
        if key not in self.keys:
            self.keys.append(key)
            self.vals.append(value)
        else:
            for i, k in enumerate(self.keys):
                if k == key:
                    self.vals[i] = value

    def get(self, key: int) -> int:
        for i, k in enumerate(self.keys):
            if k == key:
                return self.vals[i]
        
        return -1

    def remove(self, key: int) -> None:
        for i, k in enumerate(self.keys):
            if k == key:
                self.keys.pop(i)
                self.vals.pop(i)


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)