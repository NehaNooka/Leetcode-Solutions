class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        count=defaultdict(int)
        res=-1

        for num in nums:
            key=sum(int(digit) for digit in str(num))
            if key in count.keys():
                    res=max(res,count[key]+num)
                    count[key]=max(count[key],num)
            else:
                count[key]=num

        return res

        