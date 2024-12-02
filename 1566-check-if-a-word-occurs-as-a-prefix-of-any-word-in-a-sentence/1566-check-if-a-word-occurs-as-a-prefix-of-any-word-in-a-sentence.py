class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        sentence=sentence.split()
        wordLen=len(searchWord)
        for i,sent in enumerate(sentence):
            if len(sent)>=wordLen and sent[:wordLen]==searchWord: 
                return i+1
        return -1
        