class NumberContainers:

    def __init__(self):
        self.containers={} # 1:10 2:20
        self.smallestNumber={} # 10: [heap of indexes]
        
    def change(self, index: int, number: int) -> None:
        self.containers[index]=number
        if number not in self.smallestNumber:
            self.smallestNumber[number]=[] #make a new heap
        heapq.heappush(self.smallestNumber[number],index)

    def find(self, number: int) -> int:
        if number not in self.smallestNumber:
            return -1
        indexes =self.smallestNumber[number]

        while indexes:
            min_index=indexes[0]

            if self.containers[min_index]==number:
                return min_index
            heapq.heappop(indexes)
        return -1
            
# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)