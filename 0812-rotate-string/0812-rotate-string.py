class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s)!=len(goal): return False
        for i  in range(len(s)):
            if s[i+1:]+ s[:i+1] == goal:
                return True
        return False
        