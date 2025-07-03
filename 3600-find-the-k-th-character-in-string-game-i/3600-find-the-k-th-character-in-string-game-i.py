class Solution:
    def kthCharacter(self, k: int) -> str:
        start=['a']
        while len(start)<k:
            for i in range(len(start)):
                if start[i]=='z': next='a'
                else: next=chr(ord(start[i])+1)
                start.append(next)
        return start[k-1]