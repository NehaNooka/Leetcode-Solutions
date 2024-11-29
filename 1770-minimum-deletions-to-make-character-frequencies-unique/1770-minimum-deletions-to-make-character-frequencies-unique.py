class Solution:
    def minDeletions(self, s: str) -> int:
        count,res = {},0
        for c in s:
            count[c] = count.get(c, 0) + 1
        frequencies = sorted(count.values(), reverse=True)
        seen = set()
        for freq in frequencies:
            # Reduce frequency until it is unique or zero
            while freq > 0 and freq in seen:
                freq -= 1
                res += 1
            seen.add(freq)
        return res

        