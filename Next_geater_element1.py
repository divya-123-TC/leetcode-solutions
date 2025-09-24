class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ng = {}
        st = []
        for num in nums2:
            while st and st[-1] < num:
                ng[st.pop()] = num
            st.append(num)
        return [ng.get(num, -1) for num in nums1]