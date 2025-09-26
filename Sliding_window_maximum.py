class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res=[]
        q=deque()
        for idx,num in enumerate(nums):
            if q and q[0]<=idx-k:
                q.popleft()
            while q and nums[q[-1]]<num:
                q.pop()
            q.append(idx)
            if idx>=k-1:
                res.append(nums[q[0]])
        return res