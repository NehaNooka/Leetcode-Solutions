class Trie:
    def __init__(self):
        self.children={}
        self.is_end=False
    
    def add(self,word):
        cur=self
        for word in word.split('/'):
            if word not in cur.children:
                cur.children[word]=Trie()
            cur=cur.children[word]
        cur.is_end=True
    
    def prefix_search(self,word):
        cur=self
        words=word.split('/')
        for i in range(len(words)-1):
                cur=cur.children[words[i]]
                if cur.is_end:
                    return True        
        return False


class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        trie=Trie()
        for f in folder:
            trie.add(f) 
        res=[]
        for f in folder:
            if not trie.prefix_search(f):
                res.append(f)
        return res
        