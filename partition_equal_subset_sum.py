from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # If total sum is odd, we can’t split it into 2 equal parts
        if sum(nums) % 2:
            return False

        dp = set()
        dp.add(0)                      # we can always make sum 0 (by taking nothing)
        target = sum(nums) // 2        # each subset should have this sum

        # Go through the array from end to start
        for i in range(len(nums) - 1, -1, -1):
            nextDP = set()
            for t in dp:
                # If we can reach target exactly, return True early
                if (t + nums[i]) == target:
                    return True
                # Option 1: take nums[i]
                nextDP.add(t + nums[i])
                # Option 2: don’t take nums[i]
                nextDP.add(t)
            dp = nextDP

        return True if target in dp else False