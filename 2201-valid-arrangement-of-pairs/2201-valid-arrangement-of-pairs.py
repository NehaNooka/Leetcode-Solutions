class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        #Build the Graph
        graph=defaultdict(deque)
        in_degree=defaultdict(int)
        out_degree=defaultdict(int)

        for start,end in pairs:
            graph[start].append(end)
            out_degree[start]+=1
            in_degree[end]+=1
        
        #Find the starting node of eulerian path
        start_node=pairs[0][0]
        for node in graph:
            if out_degree[node]>in_degree[node]:
                start_node=node
                break
        
        #Hierholzers algo to find EUlerian path
        stack=[start_node]
        result=[]  
        while stack:
            while graph[stack[-1]]:
                next_node=graph[stack[-1]].popleft()
                stack.append(next_node)
            result.append(stack.pop())

        #format the result
        result.reverse()
        return [[result[i],result[i+1]] for i in range(len(result)-1)]

        