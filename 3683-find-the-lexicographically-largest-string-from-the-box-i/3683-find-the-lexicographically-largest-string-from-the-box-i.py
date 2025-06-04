class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        if numFriends==1: return word
        if len(word)==numFriends: return max(word)
        m=len(word)-numFriends+1
        return max(word[i:i+m] for i in range(len(word)))


        