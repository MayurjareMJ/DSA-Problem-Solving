class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)
        expected_sum = n * (n + 1) // 2
        actual_sum = sum(nums)
        return expected_sum - actual_sum



#⚡ Alternative Optimal (Using XOR):

#If you prefer bit manipulation, XOR also gives an O(n), O(1) solution:

class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)
        xor_all = 0
        for i in range(n + 1):
            xor_all ^= i
        for num in nums:
            xor_all ^= num
        return xor_all