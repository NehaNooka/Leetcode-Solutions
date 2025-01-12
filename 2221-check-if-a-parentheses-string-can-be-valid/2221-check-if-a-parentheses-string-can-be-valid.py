class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s)%2: return False
        locked_stack=[]
        unlocked_stack=[]
        for i in range(len(s)):
            if locked[i]=='0':
                unlocked_stack.append(i)
            elif s[i]=='(':
                locked_stack.append(i)
            else:
                if locked_stack: locked_stack.pop()
                elif unlocked_stack: unlocked_stack.pop()
                else: return False
        
        while locked_stack and unlocked_stack and locked_stack[-1]<unlocked_stack[-1]:
            locked_stack.pop()
            unlocked_stack.pop()
        if locked_stack: return False
        return True