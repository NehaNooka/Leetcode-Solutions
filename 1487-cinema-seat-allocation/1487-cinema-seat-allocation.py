import collections
class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        RS = collections.defaultdict(set)
        for row, seat in reservedSeats:
            RS[row].add(seat)
        
        res = (n - len(RS)) * 2
        
        for row, reserved in RS.items():
            left = all(seat not in reserved for seat in [2, 3, 4, 5])
            middle = all(seat not in reserved for seat in [4, 5, 6, 7])
            right = all(seat not in reserved for seat in [6, 7, 8, 9])
            
            if left and right:
                res += 2
            elif left or middle or right:
                res += 1
        
        return res


        