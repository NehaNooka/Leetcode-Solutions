class MyHashSet:

    def __init__(self):
        self.n=1000
        self.arr=[[] for _ in range(self.n)]
        

    def add(self, key: int) -> None:
        idx=key%self.n
        if key not in self.arr[idx]:
            self.arr[idx].append(key)
        

    def remove(self, key: int) -> None:
        idx=key%self.n
        if key in self.arr[idx]:
            self.arr[idx].remove(key)
        

    def contains(self, key: int) -> bool:
        idx=key%self.n
        return key in self.arr[idx]
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)