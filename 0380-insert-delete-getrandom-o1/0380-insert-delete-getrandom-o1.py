class RandomizedSet:

    def __init__(self):
        self.nList=[]
        self.nDict={}

    def insert(self, val: int) -> bool:
        res= val not in self.nDict
        if res:
            self.nDict[val]=len(self.nList)
            self.nList.append(val)
        return res
    
    def remove(self,val: int) -> bool:
        res=val in self.nDict
        if res: #[1,2,3,4] 2
            index=self.nDict[val]
            new_val=self.nList[-1]
            self.nList[index]=new_val
            self.nList.pop()
            self.nDict[new_val]=index
            del self.nDict[val]
        return res
        

    def getRandom(self) -> int:
        return random.choice(self.nList)   


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()