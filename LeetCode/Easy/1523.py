# 1523. Count Odd Numbers in an Interval Range
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# Given two non-negative integers low and high. Return the count of odd numbers between low and high (inclusive).

 

# Example 1:

# Input: low = 3, high = 7
# Output: 3
# Explanation: The odd numbers between 3 and 7 are [3,5,7].
# Example 2:

# Input: low = 8, high = 10
# Output: 1
# Explanation: The odd numbers between 8 and 10 are [9].


class Solution:
    def countOdds(self, low: int, high: int) -> int:
        return (high+1)//2-(low//2)
    

# 1. Naive (Brute Force)

# Loop through every number in [low, high]

# Check i % 2 != 0

# Count odds

class Solution:
    def countOdds(self, low: int, high: int) -> int:
        count = 0
        for i in range(low, high + 1):
            if i % 2 != 0:
                count += 1
        return count


# Time Complexity: O(n) where n = high - low + 1
# Space Complexity: O(1)




# 2. Math Formula (Case-Based)

# We know every two consecutive numbers contain exactly 1 odd.

# So:

# If both low and high are even → (high - low) // 2

# Otherwise → (high - low) // 2 + 1

class Solution:
    def countOdds(self, low: int, high: int) -> int:
        return ((high - low) // 2) + (1 if (low % 2 != 0 or high % 2 != 0) else 0)


# Time Complexity: O(1)
# Space Complexity: O(1)
# ✅ Very efficient and easy to understand.




# 3. Prefix Count Method (Best & Cleanest)

# Instead of conditions, use prefix counts:
# Number of odds from 1 to x = (x + 1) // 2.

# So odds in [low, high] = (high + 1)//2 - (low // 2)

class Solution:
    def countOdds(self, low: int, high: int) -> int:
        return (high + 1) // 2 - (low // 2)


# Time Complexity: O(1)
# Space Complexity: O(1)
# ✅ Shortest and cleanest formula.
# This is the one most people use in competitive coding.




# 4. Bitwise Trick (Fun Alternative)

# Odd numbers are just numbers with the last bit = 1.
# So, count of odds up to x = (x >> 1) + (x & 1)

class Solution:
    def countOdds(self, low: int, high: int) -> int:
        def odd_count(x):
            return (x >> 1) + (x & 1)
        return odd_count(high) - odd_count(low - 1)


Time Complexity: O(1)
Space Complexity: O(1)
✅ Same result, but more low-level & efficient for bit manipulation lovers.