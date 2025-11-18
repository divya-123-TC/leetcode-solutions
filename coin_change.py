class Solution:
def coinChange(self, coins:List[int], amount: int)->int:
dp = [amount + 1] * (amount + 1)
dp[0] = 0
for a in range(L,amount + 1):for c in coins:
if a-c>= 0:
dp[a] = min(dp[a], 1 + dpla -c])
return dp[amount]if dp[amount]amount + 1 else -1