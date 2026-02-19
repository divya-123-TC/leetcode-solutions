class Solution:
    def numTilings(self, n: int) -> int:
        mod=10**9+7
        if n==1:
            return 1
        if n==2:
            return 2
        if n==3:
            return 5
        a,b,c=1,2,5
        for i in range(4,n+1):
            d=(2*c+a)%mod
            a,b,c=b,c,d
        return  c