class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        res=[]
        for i in range(len(words)):
            if words[i][0] in 'aeiou' and words[i][-1] in 'aeiou':
                words[i]=1
            else:   words[i]=0
        
        prefix_sum=[0]*(len(words)+1)
        for i in range(len(words)):
            prefix_sum[i+1]=prefix_sum[i]+words[i]

        for start,end in queries:
            res.append(prefix_sum[end+1]-prefix_sum[start])
        return res
        
        


        