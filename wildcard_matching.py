class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo={}
        new_p=[]
        for ch in p:
            if not(new_p and new_p[-1]=="*" and ch=="*"):
                new_p.append(ch)
        p="".join(new_p)
        def solve(i,j):
            if (i,j) in memo:
                return memo[(i,j)]
            if j==len(p):
                return i==len(s)
            first_match=i<len(s) and (p[j]==s[i] or p[j]=="?")
            if p[j]=="*":
                result=solve(i,j+1) or (i<len(s)) and solve(i+1,j)
            else:
                result=first_match and solve(i+1,j+1)
            memo[(i,j)]=result
            return result
        return solve(0,0)