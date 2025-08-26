class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res=nums[0]
        total=0
        for n in nums:
            total+=n
            if total<0:
                total=0
            res=max(res,total)
        return res
