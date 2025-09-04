class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        diffX,diffY=abs(x-z),abs(y-z)
        if diffX< diffY: return 1
        elif diffY<diffX: return 2
        else: return 0
        