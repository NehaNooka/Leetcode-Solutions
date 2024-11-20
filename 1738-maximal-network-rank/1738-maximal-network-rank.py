class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        if not roads:
            return 0

        count = {}
        road_set = set()
        
        for a, b in roads:
            count[a] = 1 + count.get(a, 0)
            count[b] = 1 + count.get(b, 0)
            road_set.add((min(a, b), max(a, b)))
        res = 0

        for i in range(n - 1):
            for j in range(i + 1, n):
                if (i, j) in road_set:
                    res = max(res, count.get(i, 0) + count.get(j, 0) - 1)
                else:
                    res = max(res, count.get(i, 0) + count.get(j, 0))
        
        return res
