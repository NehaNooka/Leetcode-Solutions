class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort()

        min_heap=[]
        i=0
        n=len(events)
        count=0
        last_day=max(end for _,end in events)

        for day in range(1,last_day+1):
            while i<n and events[i][0]==day:
                heapq.heappush(min_heap,events[i][1])
                i+=1

            while min_heap and min_heap[0]<day:
                heapq.heappop(min_heap)

            if min_heap:
                heapq.heappop(min_heap)
                count+=1
            if i==n and not min_heap:
                break
        return count                