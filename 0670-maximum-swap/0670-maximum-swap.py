class Solution:
    def maximumSwap(self, num: int) -> int:
        num=list(str(num))
        max_arr=[0]*len(num)
        max_arr[-1]=(num[-1],len(num)-1)
        for i in range(len(num)-2,-1,-1):
            if int(max_arr[i+1][0])>= int(num[i]):
                max_arr[i]=max_arr[i+1]
            else:
                max_arr[i]=(num[i],i)

        # [2,7,3,6], [(7,1),(7,1),(6,3),(6,3)]
        for i in range(len(num)):
            if int(num[i])<int(max_arr[i][0]):
                num[i],num[max_arr[i][1]]=num[max_arr[i][1]],num[i]
                break

        return int(''.join(num))



        