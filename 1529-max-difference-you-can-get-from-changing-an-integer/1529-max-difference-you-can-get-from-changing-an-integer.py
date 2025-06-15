class Solution:
    def maxDiff(self, num: int) -> int:
        # Step 1: Convert num to string (list for easier char substitution)
        s = list(str(num))

        # Step 2: Make the max version by replacing a digit with 9
        for d in s:
            if d != '9':
                # Replace all occurrences of d with '9'
                max_s = ''.join('9' if c == d else c for c in s)
                break
        else:
            # If all digits are already 9
            max_s = ''.join(s)

        # Step 3: Make the min version
        if s[0] != '1':
            # Replace all instances of first digit with '1'
            d = s[0]
            min_s = ''.join('1' if c == d else c for c in s)
        else:
            # Look for first digit after first that is not 0 or 1
            for d in s[1:]:
                if d != '0' and d != '1':
                    min_s = ''.join('0' if c == d else c for c in s)
                    break
            else:
                # If no such digit found
                min_s = ''.join(s)

        # Step 4: Convert to integers
        max_num = int(max_s)
        min_num = int(min_s)

        # Step 5: Return the difference
        return max_num - min_num