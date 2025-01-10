class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        count2=defaultdict(int)
        for w in words2:
            countW=Counter(w)
            for c,cnt in  countW.items():
                count2[c]=max(count2[c],cnt)
        res=[]
        for w in words1:
            countW=Counter(w)
            flag=True
            for c,cnt in count2.items():
                if countW[c]< cnt:
                    flag=False
                    break
            if flag: res.append(w)
        return res
            

        