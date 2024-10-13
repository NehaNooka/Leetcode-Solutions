class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r=0,len(nums)-1

        while l<=r:
            mid= (l+r) // 2
            if target==nums[mid]:
                return mid
            
            #left [4,5,6,7,0,1,2]
            if nums[l] <= nums[mid]:
                if target > nums[mid] or target < nums[l]:
                    l=mid+1
                else:
                    r=mid-1

            #right [4,5,6,7,0,1,2]
            else:
                if target < nums[mid] or target > nums[r]:
                    r=mid-1
                else:
                    l=mid+1
        return -1
            