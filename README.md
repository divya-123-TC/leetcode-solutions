# leetcode-solutions
My Leetcode practice problems



## Two Sum Problem

### Problem Description
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.  
You may assume that each input would have *exactly one solution*, and you may not use the same element twice.  
You can return the answer in any order.



### Solution Explanation

The solution uses a hashmap (dictionary) to store each number's index while iterating through the list.  
- First, it stores all numbers and their indices in the hashmap.  
- Then, it iterates through the list again, calculates the complement (target - current_number), and checks if the complement exists in the hashmap and is not the same element.  
- If found, it returns the indices of the current number and its complement.

This approach has a time complexity of *O(n)* because it uses two passes through the list with constant time dictionary lookups.
