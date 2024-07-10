class Solution:
    def minOperations(self, logs: List[str]) -> int:
        folderLevel=0
        for log in logs:
            if folderLevel > 0 and log=="../":
                folderLevel-=1
            elif folderLevel==0 and log=="../" or log=="./":
                pass
            else:
                folderLevel+=1
            
        return folderLevel
        