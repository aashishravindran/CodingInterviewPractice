# 153. Find Minimum in Rotated Sorted Array
# Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

# [4,5,6,7,0,1,2] if it was rotated 4 times.
# [0,1,2,4,5,6,7] if it was rotated 7 times.
# Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

# Given the sorted rotated array nums of unique elements, return the minimum element of this array.

# You must write an algorithm that runs in O(log n) time.

from typing import List

## Intuition and Explanation

# Key Insight: Understanding the structure of a rotated sorted array
# When a sorted array is rotated, it creates two sorted subarrays:
# - Left subarray: [larger elements] 
# - Right subarray: [smaller elements]
# - Minimum (0) is at the inflection point between these two subarrays

# Example: [4,5,6,7,0,1,2] (rotated 4 times)
# - Left: [4,5,6,7] (larger elements)
# - Right: [0,1,2] (smaller elements)
# - Minimum (0) is at the inflection point between these two subarrays

# Why Binary Search Works:
# 1. The minimum element is always at the inflection point (boundary between larger and smaller subarrays)
# 2. We can use binary search by comparing the middle element with the rightmost element
# 3. This comparison tells us which half contains the minimum

# Binary Search Strategy:
# - Compare nums[mid] with nums[right] (rightmost element)
# - If nums[mid] > nums[right]: minimum is in right half (after mid)
# - If nums[mid] <= nums[right]: minimum is in left half (including mid)

# Why Compare with Right Element?
# - The rightmost element is always in the "smaller" sorted subarray
# - It provides a reliable reference point regardless of rotation count
# - This comparison works for any number of rotations

# Example Walkthrough: [4,5,6,7,0,1,2]
# Initial: left=0, right=6, mid=3, nums[mid]=7, nums[right]=2
# Since 7 > 2, minimum is in right half: left = mid + 1 = 4
# Now: left=4, right=6, mid=5, nums[mid]=1, nums[right]=2  
# Since 1 <= 2, minimum is in left half: right = mid = 5
# Now: left=4, right=5, mid=4, nums[mid]=0, nums[right]=1
# Since 0 <= 1, minimum is in left half: right = mid = 4
# Now: left=4, right=4, loop ends, return nums[4] = 0

## Solutions

class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        O(log n) solution using binary search
        """
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        return nums[left]
    
    def findMin_brute_force(self, nums: List[int]) -> int:
        """
        O(n) solution using linear search
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        min_val = nums[0]
        for num in nums:
            if num < min_val:
                min_val = num
        return min_val
    
    def findMin_quadratic(self, nums: List[int]) -> int:
        """
        O(n²) solution using nested loops to find minimum
        Time Complexity: O(n²) 
        Space Complexity: O(1)
        This is intentionally inefficient for demonstration purposes
        """
        min_val = nums[0]
        for i in range(len(nums)):
            for j in range(len(nums)):
                # Compare each element with every other element
                if nums[i] <= nums[j] and nums[i] < min_val:
                    min_val = nums[i]
        return min_val

## Test Cases

def run_tests():
    """
    Comprehensive test suite for all solutions
    """
    test_cases = [
        # Basic cases
        ([3, 4, 5, 1, 2], 1),
        ([4, 5, 6, 7, 0, 1, 2], 0),
        ([11, 13, 15, 17], 11),
        
        # Edge cases
        ([1], 1),
        ([2, 1], 1),
        ([1, 2], 1),
        
        # Multiple rotations
        ([0, 1, 2, 4, 5, 6, 7], 0),  # No rotation
        ([7, 0, 1, 2, 4, 5, 6], 0),  # Rotated 1 time
        ([6, 7, 0, 1, 2, 4, 5], 0),  # Rotated 2 times
        ([5, 6, 7, 0, 1, 2, 4], 0),  # Rotated 3 times
        
        # Larger arrays
        ([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 1, 2, 3, 4, 5, 6, 7, 8, 9], 1),
        ([100, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 30, 40, 50, 60, 70, 80, 90], 1),
    ]
    
    solutions = [
        ("Binary Search (O(log n))", Solution().findMin),
        ("Linear Search (O(n))", Solution().findMin_brute_force),
        ("Quadratic Search (O(n²))", Solution().findMin_quadratic),
    ]
    
    print("Running comprehensive tests...")
    print("=" * 60)
    
    for solution_name, solution_func in solutions:
        print(f"\nTesting {solution_name}:")
        print("-" * 40)
        
        all_passed = True
        for i, (nums, expected) in enumerate(test_cases):
            try:
                result = solution_func(nums)
                status = "✓ PASS" if result == expected else "✗ FAIL"
                print(f"Test {i+1}: {status} | Input: {nums} | Expected: {expected} | Got: {result}")
                if result != expected:
                    all_passed = False
            except Exception as e:
                print(f"Test {i+1}: ✗ ERROR | Input: {nums} | Error: {e}")
                all_passed = False
        
        if all_passed:
            print(f"\n✅ All tests passed for {solution_name}")
        else:
            print(f"\n❌ Some tests failed for {solution_name}")
    
    print("\n" + "=" * 60)
    print("Test Summary:")
    print("- Binary Search: Most efficient, O(log n) time complexity")
    print("- Linear Search: Simple but O(n) time complexity") 
    print("- Quadratic Search: Inefficient O(n²) time complexity (for demonstration)")

if __name__ == "__main__":
    run_tests()