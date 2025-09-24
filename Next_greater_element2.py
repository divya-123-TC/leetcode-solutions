class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n=len(nums)
        ng=[-1]*n
        st=[]
        for i in range(2*n):
            num=nums[i%n]
            while st and nums[st[-1]]<num:
                ng[st.pop()]=num
            if i<n:
                st.append(i)
        return ng