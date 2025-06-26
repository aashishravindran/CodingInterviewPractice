"""
https://leetcode.com/problems/maximum-subarray/description/

Given an integer array nums, find the subarray with the largest sum, and return its sum.
"""

# ---
#
# ## Kadane's Algorithm: Explanation and Why It Works
#
# Kadane's Algorithm is an efficient way to solve the maximum subarray sum problem in O(n) time.
#
# **How it works:**
# - We iterate through the array, maintaining two variables:
#   - `current_sum`: the sum of the current subarray (ending at the current index)
#   - `max_sum`: the maximum sum found so far
# - For each element, we add it to `current_sum`.
# - If `current_sum` becomes greater than `max_sum`, we update `max_sum`.
# - If `current_sum` drops below 0, we reset it to 0. This is because any subarray starting before this point would have a lower sum than starting fresh from the next element.
#
# **Why it works:**
# - If the running sum (`current_sum`) is negative, adding it to any future element will only decrease the sum. So, it's optimal to start a new subarray from the next element.
# - By always keeping track of the best sum so far (`max_sum`), we ensure we never miss the optimal subarray.
# - This greedy approach guarantees that we find the maximum sum in a single pass.
#
# **Example:**
# For nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]:
# - At each step, we either extend the current subarray or start a new one if the sum drops below zero.
# - The algorithm finds the subarray [4, -1, 2, 1] with sum 6.
#
# ---
#
# ## Why Kadane's Algorithm Works (with Visual Representation)
#
# Kadane's Algorithm maintains a running sum (`current_sum`) and a global maximum (`max_sum`).
# - If `current_sum` becomes negative, it is reset to 0, because any subarray starting before this point would be worse than starting fresh.
# - At each step, we update `max_sum` if `current_sum` is greater.
#
# ### Visual Example
#
# Suppose nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
#
# Step-by-step:
#
# | Index | Num | Current Sum | Max Sum | Action                |
# |-------|-----|-------------|---------|-----------------------|
# | 0     | -2  | -2          | -2      | Start, set both       |
# | 1     | 1   | 1           | 1       | Reset, new max        |
# | 2     | -3  | -2          | 1       | Reset                 |
# | 3     | 4   | 4           | 4       | Reset, new max        |
# | 4     | -1  | 3           | 4       | Continue              |
# | 5     | 2   | 5           | 5       | New max               |
# | 6     | 1   | 6           | 6       | New max               |
# | 7     | -5  | 1           | 6       | Continue              |
# | 8     | 4   | 5           | 6       | Continue              |
#
# The largest sum is 6, from subarray [4, -1, 2, 1].
#
# ---
#
# ## Brute Force Solution
#
# The brute force approach checks all possible subarrays and computes their sums, keeping track of the maximum.
#
# Time Complexity: O(n^2)
#
# ---

from typing import List, Tuple

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        current_sum = 0
        for num in nums:
            current_sum += num
            if current_sum > max_sum:
                max_sum = current_sum
            if current_sum < 0:
                current_sum = 0
        return max_sum

    def maxSubArrayPrint(self, nums: List[int]) -> Tuple[int, List[int]]:
        max_sum = nums[0]
        res = []
        current_sum = 0
        left = 0
        for right, num in enumerate(nums):
            current_sum += num
            if current_sum > max_sum:
                max_sum = current_sum
                res = nums[left:right+1]
            if current_sum < 0:
                current_sum = 0
                # When the running sum drops below zero, we start a new subarray from the next index.
                # This ensures we don't include the negative-sum prefix in the next candidate subarray.
                left = right + 1  # Move left pointer to the next index
        return max_sum, res

    def maxSubArrayBruteForce(self, nums: List[int]) -> int:
        max_sum = nums[0]
        n = len(nums)
        for i in range(n):
            current_sum = 0
            for j in range(i, n):
                current_sum += nums[j]
                if current_sum > max_sum:
                    max_sum = current_sum
        return max_sum


def main():
    test_cases = [
        ([-2,1,-3,4,-1,2,1,-5,4], 6),
        ([1], 1),
        ([5,4,-1,7,8], 23),
        ([-1,-2,-3,-4], -1),
        ([0,0,0,0], 0),
    ]
    sol = Solution()
    print("Testing Kadane's Algorithm:")
    for nums, expected in test_cases:
        result = sol.maxSubArray(nums)
        print(f"Input: {nums}\nExpected: {expected}, Got: {result}\n")
        assert result == expected
    print("\nTesting Brute Force Solution:")
    for nums, expected in test_cases:
        result = sol.maxSubArrayBruteForce(nums)
        print(f"Input: {nums}\nExpected: {expected}, Got: {result}\n")
        assert result == expected
    print("\nTesting Kadane's Algorithm (Print Subarray):")
    for nums, expected in test_cases:
        max_sum, subarray = sol.maxSubArrayPrint(nums)
        print(f"Input: {nums}\nMax Sum: {max_sum}, Subarray: {subarray}\n")
        assert max_sum == expected
    print("\nAll tests passed!")

if __name__ == "__main__":
    main()

    
    
    