class Solution:
    def myAtoi(self, s: str) -> int:
        if not s:
            return 0
        i=0
        n=len(s)
        Int_max=2**31-1
        Int_min=-2**31
        while i<n and s[i]==" ":
            i+=1
        if i==n:
            return 0
        sign=1
        if s[i]=="+":
            i+=1
        elif s[i]=="-":
            sign=-1
            i+=1
        res=0
        while i<n and s[i].isdigit():
            digit=int(s[i])
            res=res*10+digit
            if res*sign<=Int_min:
                return Int_min
            if res*sign>=Int_max:
                return Int_max
            i+=1
        return res*sign