class TrieNode:
    def __init__(self):
        self.children={}
        self.counts=0
    
    def insert(self,word):
        cur=self
        for c in word:
            if c not in cur.children:
                cur.children[c]=TrieNode()
            cur=cur.children[c]
            cur.counts+=1

    def search(self,word):
        res=0
        cur=self
        for c in word:
            cur=cur.children[c]
            res+=cur.counts
        return res

class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        res=[]
        root=TrieNode()
        for word in words:
            root.insert(word)
 
        for word in words:
            res.append(root.search(word))
        return res
        