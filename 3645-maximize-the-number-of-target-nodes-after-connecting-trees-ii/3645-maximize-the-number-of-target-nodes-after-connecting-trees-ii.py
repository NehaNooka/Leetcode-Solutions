class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:
        def makeAdj(edges, n):
            mat = [[] for _ in range(n)]
            for u, v in edges:
                mat[u].append(v)
                mat[v].append(u)
            return mat

        def colour(graph, n):
            color = [-1] * n
            cnt = [0, 0]

            def dfs(node, c):
                color[node] = c
                cnt[c] += 1
                for dest in graph[node]:
                    if color[dest] == -1:
                        dfs(dest, 1 - c)

            dfs(0, 0)
            return color, cnt

        n = len(edges1) + 1
        m = len(edges2) + 1

        g1 = makeAdj(edges1, n)
        g2 = makeAdj(edges2, m)

        c1, cnt1 = colour(g1, n)
        c2, cnt2 = colour(g2, m)

        max2 = max(cnt2[0], cnt2[1])

        targets = []
        for i in range(n):
            c = c1[i]
            same = cnt1[c]
            targets.append(same + max2)

        return targets