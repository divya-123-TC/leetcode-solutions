class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda x:(x[0],-x[1]))
        heights=[h for _,h in envelopes]
        import bisect
        dp=[]
        for h in heights:
            pos=bisect.bisect_left(dp,h)
            if pos==len(dp):
                dp.append(h)
            else:
                dp[pos]=h
        return len(dp)