class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        return True if Counter(target)== Counter(arr) else False
        