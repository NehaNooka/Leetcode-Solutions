class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        wordList.append(beginWord)
        nei=collections.defaultdict(list)
        for word in wordList:
            for j in range(len(word)):
                pattern= word[:j]+'*'+word[j+1:]
                nei[pattern].append(word)

        visit=set([beginWord])
        queue=deque([beginWord])
        res=1
        while queue:
            for i in range(len(queue)):
                word=queue.popleft()
                if word == endWord: return res 

                for j in range(len(word)):
                    pattern= word[:j]+'*'+word[j+1:]
                    for neighbor in nei[pattern]:
                        if neighbor not in visit:
                            visit.add(neighbor)
                            queue.append(neighbor)
            res+=1
        return 0