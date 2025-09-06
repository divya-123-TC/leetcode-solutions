class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len=0
        left=0
        last_seen={}
        for right,c in  enumerate(s):
            if c in last_seen and last_seen[c]>=left:
                left=last_seen[c]+1
                max_len=max(max_len,right-left+1)
            last_seen[c]=right
        return max_len