class Solution:
    def partition(self, s: str):
        res = []
        n = len(s)
        memo = {}

        def is_palindrome(sub):
            return sub == sub[::-1]

        def dfs(start):
            if start == n:
                return [[]]  # one valid partition (end reached)
            if start in memo:
                return memo[start]

            partitions = []
            for end in range(start + 1, n + 1):
                prefix = s[start:end]
                if is_palindrome(prefix):
                    for rest in dfs(end):
                        partitions.append([prefix] + rest)
            memo[start] = partitions
            return partitions

        return dfs(0)