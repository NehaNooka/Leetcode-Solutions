class Solution:
    def kthCharacter(self, k: int) -> str:
        start=['a']
        while len(start)<k:
            for i in range(len(start)):
                next= chr(ord('a')+ ((ord(start[i])-ord('a')+1)%26))
                start.append(next)
        return start[k-1]