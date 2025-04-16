class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        freq=defaultdict(int)
        left,pair_cnt, res=0,0,0

        for right in range(len(nums)):
            pair_cnt+=freq[nums[right]]
            freq[nums[right]]+=1

            while pair_cnt>=k:
                res+=len(nums)-right
                freq[nums[left]]-=1
                pair_cnt-=freq[nums[left]]
                left+=1
        return res

        