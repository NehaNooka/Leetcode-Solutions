import heapq

class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        max_heap = []
        min_heap = []

        queries.sort()
        query_index = 0

        chosen_queries = 0

        for i in range(len(nums)):
            while query_index < len(queries) and queries[query_index][0] == i:
                heapq.heappush(max_heap, -queries[query_index][1])
                query_index += 1
            
            while max_heap and -max_heap[0] >= i:
                if len(min_heap) >= nums[i]:
                    break

                chosen_queries += 1
                heapq.heappush(min_heap, -heapq.heappop(max_heap))
            
            if len(min_heap) < nums[i]:
                return -1
            
            while min_heap and min_heap[0] == i:
                heapq.heappop(min_heap)
        
        return len(queries) - chosen_queries