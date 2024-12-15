class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        max_heap=[]

        def cal_increment(pass_stud,total_stud):
            cur_avg=pass_stud/total_stud
            new_avg=(pass_stud+1)/(total_stud+1)
            return new_avg-cur_avg


        for i,(pass_stud,total_stud) in enumerate(classes):
            inc=cal_increment(pass_stud,total_stud)     
            heapq.heappush(max_heap,(-1*inc,i))
        
        while extraStudents:
            _,idx=heapq.heappop(max_heap)
            classes[idx][0]+=1
            classes[idx][1]+=1
            inc=cal_increment(classes[idx][0],classes[idx][1])
            heapq.heappush(max_heap,(-1*inc,idx))
            extraStudents-=1

        final_avg=sum(c[0]/c[1] for c in classes)
        return final_avg/len(classes)   