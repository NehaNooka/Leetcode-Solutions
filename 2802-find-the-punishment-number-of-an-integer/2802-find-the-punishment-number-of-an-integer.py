class Solution:
    def punishmentNumber(self, n: int) -> int:
        res = 0

        def canPartition(sq: str, target: int) -> bool:
            def backtrack(index, current_sum):
                if index == len(sq):
                    return current_sum == target
                for j in range(index + 1, len(sq) + 1):
                    num = int(sq[index:j])
                    if backtrack(j, current_sum + num):
                        return True
                return False
            return backtrack(0, 0)

        for i in range(1, n + 1):
            sq = i * i
            if canPartition(str(sq), i):
                res += sq
        return res