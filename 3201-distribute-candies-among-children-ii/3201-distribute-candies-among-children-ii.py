class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        def S(m):
            return comb(m + 2, 2) if m >= 0 else 0

        total = S(n)
        total -= 3 * S(n - limit - 1)
        total += 3 * S(n - 2 * (limit + 1))
        total -= S(n - 3 * (limit + 1))
        return total
        