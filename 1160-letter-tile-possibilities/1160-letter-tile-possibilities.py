class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        def backtrack(counter):
            total = 0
            for char in counter:
                if counter[char] > 0:
                    # Use the current character
                    counter[char] -= 1
                    total += 1 + backtrack(counter)  # Count this sequence and recurse
                    # Backtrack: restore the character count
                    counter[char] += 1
            return total

        counter = Counter(tiles)
        return backtrack(counter)
        