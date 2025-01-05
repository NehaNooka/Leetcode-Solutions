class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        shift_array = [0] * (n + 1)  # Difference array
        
        # Apply shifts to the difference array
        for start, end, direction in shifts:
            if direction == 1:
                shift_array[start] += 1
                shift_array[end + 1] -= 1
            else:
                shift_array[start] -= 1
                shift_array[end + 1] += 1

        # Calculate the net shifts
        for i in range(1, n):
            shift_array[i] += shift_array[i - 1]
        
        # Apply shifts to characters
        result = []
        for i, c in enumerate(s):
            shift = shift_array[i]
            new_char = chr((ord(c) - ord('a') + shift) % 26 + ord('a'))
            result.append(new_char)
        
        return ''.join(result)

        