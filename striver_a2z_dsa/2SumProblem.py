from typing import List

## https://leetcode.com/problems/two-sum/description/
"""

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.


Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 
Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
 

Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
"""

class Solution:
    def twoSumBruteForce(self, nums: List[int], target: int) -> List[int]:
          """
            Simply iterate over the array and check if the sum of the current element and the next element is equal to the target.
            If it is, return the indices of the two elements.
            If it is not, return -1.
          """
          for i in range(len(nums)):
            for j in range(i+1, len(nums)):
              if nums[i] + nums[j] == target:
                return [i, j]
          return []
    def twoSumOptimizedNLogN(self, nums: List[int], target: int) -> List[int]:
        """
        sort the array and use two pointers and use Binary Search to find the target 
        """
        nums.sort()

        start,end = 0, len(nums)-1
        while start < end:
            if nums[start] + nums[end] == target:
                return [start, end]
            elif nums[start] + nums[end] < target:
                start += 1
            else:
                end -= 1
        return []
    def twoSumOptimizedN(self, nums: List[int], target: int) -> List[int]:
        """
        use a hashmap to store the elements 
        In every iternation we check if the target - current element is in the hashmap
        if so we return the indices . Else store nums[i] = i in the hashmap
        if we reach the end of the array and we don't find the target we return -1
        ### Why does this work?

        
        """
        hashmap = {}
        
        for i, num in enumerate(nums):
            complement = target - num
            
            # If complement exists in hashmap, we found our pair
            if complement in hashmap:
                return [hashmap[complement], i]
            
            # Store current number and its index
            hashmap[num] = i
        
        return []  # No solution found

        """
        DETAILED EXPLANATION OF WHY THE OPTIMIZED O(n) SOLUTION WORKS:
        
        The algorithm is based on a simple mathematical principle: if we need to find two numbers 
        that sum to 'target', then for any number 'num' in the array, its complement must be 'target - num'.
        
        KEY INSIGHT: Instead of looking for pairs by comparing every element with every other element (O(n²)), 
        we can:
        1. For each number, calculate what its "partner" should be
        2. Check if we've already seen that partner earlier in the array
        3. If yes, we've found our pair!
        
        STEP-BY-STEP WALKTHROUGH (Example: nums = [2, 7, 11, 15], target = 9):
        
        Iteration 1: i=0, num=2
        - complement = target - num = 9 - 2 = 7
        - Is 7 in hashmap? No (hashmap is empty)
        - Store hashmap[2] = 0
        - Hashmap: {2: 0}
        
        Iteration 2: i=1, num=7
        - complement = target - num = 9 - 7 = 2
        - Is 2 in hashmap? Yes! (hashmap[2] = 0)
        - Found our pair! Return [hashmap[2], 1] = [0, 1]
        
        WHY THIS GUARANTEES CORRECTNESS:
        1. Completeness: If a solution exists, we will find it because when we encounter the second 
           number of a valid pair, its complement (the first number) will already be in the hashmap.
        2. Uniqueness: We only use each element once because we check for the complement before 
           adding the current number to the hashmap.
        3. Order Preservation: We return [hashmap[complement], i] where hashmap[complement] is the 
           index of the first number (smaller index) and i is the index of the second number (larger index).
        
        TIME AND SPACE COMPLEXITY:
        - Time Complexity: O(n) - we traverse the array only once
        - Space Complexity: O(n) - in the worst case, we might store all elements in the hashmap
        
        WHY THIS IS OPTIMAL:
        1. Lower Bound: We must examine each element at least once to find a solution, so O(n) is the best possible time complexity.
        2. Hashmap Operations: complement in hashmap and hashmap[num] = i are both O(1) average case.
        3. Single Pass: Unlike the brute force approach that needs nested loops, this algorithm processes each element exactly once.
        
        EDGE CASES HANDLED:
        1. Duplicate Elements: Works correctly because we check for complements before adding current element.
        2. No Solution: Returns empty list if no valid pair exists.
        3. Single Solution: Guaranteed to find the unique solution as per problem constraints.
        """

def main():
    """
    Main function to test all three implementations of the Two Sum problem
    """
    solution = Solution()
    
    # Test cases from the problem description
    test_cases = [
        {
            "nums": [2, 7, 11, 15],
            "target": 9,
            "expected": [0, 1],
            "description": "Example 1: Basic case"
        },
        {
            "nums": [3, 2, 4],
            "target": 6,
            "expected": [1, 2],
            "description": "Example 2: Target in middle"
        },
        {
            "nums": [3, 3],
            "target": 6,
            "expected": [0, 1],
            "description": "Example 3: Duplicate elements"
        },
        {
            "nums": [1, 5, 8, 10, 13, 17],
            "target": 18,
            "valid_pairs": [[0, 5], [2, 3], [2, 5], [3, 4]],  # All valid pairs possible
            "description": "Larger array test"
        },
        {
            "nums": [-1, -2, -3, -4, -5],
            "target": -8,
            "expected": [2, 4],
            "description": "Negative numbers"
        },
        {
            "nums": [0, 4, 3, 0],
            "target": 0,
            "expected": [0, 3],
            "description": "Zero values"
        },
        {
            "nums": [1, 2, 3, 4, 5],
            "target": 9,
            "expected": [3, 4],
            "description": "Consecutive numbers"
        }
    ]
    
    # Test all three implementations
    implementations = [
        ("Brute Force", solution.twoSumBruteForce),
        ("Optimized O(n)", solution.twoSumOptimizedN)
    ]
    
    for impl_name, impl_func in implementations:
        print(f"\n{'='*60}")
        print(f"Testing {impl_name} Implementation")
        print(f"{'='*60}")
        
        all_passed = True
        
        for i, test_case in enumerate(test_cases, 1):
            nums = test_case["nums"].copy()  # Create a copy to avoid modifying original
            target = test_case["target"]
            description = test_case["description"]
            
            try:
                result = impl_func(nums, target)
                
                # Check if result is correct
                is_valid = False
                if "expected" in test_case:
                    # For cases with single expected result
                    if set(result) == set(test_case["expected"]):
                        is_valid = True
                elif "valid_pairs" in test_case:
                    # For cases with multiple valid pairs
                    for valid_pair in test_case["valid_pairs"]:
                        if set(result) == set(valid_pair):
                            is_valid = True
                            break
                
                if is_valid:
                    print(f"✓ Test {i}: {description}")
                    print(f"  Input: nums = {test_case['nums']}, target = {target}")
                    print(f"  Output: {result}")
                    if "expected" in test_case:
                        print(f"  Expected: {test_case['expected']}")
                    else:
                        print(f"  Valid pairs: {test_case['valid_pairs']}")
                else:
                    print(f"✗ Test {i}: {description}")
                    print(f"  Input: nums = {test_case['nums']}, target = {target}")
                    print(f"  Output: {result}")
                    if "expected" in test_case:
                        print(f"  Expected: {test_case['expected']}")
                    else:
                        print(f"  Valid pairs: {test_case['valid_pairs']}")
                    all_passed = False
                    
            except Exception as e:
                print(f"✗ Test {i}: {description} - ERROR: {e}")
                all_passed = False
            
            print()
        
        if all_passed:
            print(f"🎉 All tests passed for {impl_name}!")
        else:
            print(f"❌ Some tests failed for {impl_name}")
    
    # Test O(n log n) implementation separately since it has different behavior
    print(f"\n{'='*60}")
    print("Testing Optimized O(n log n) Implementation")
    print("Note: This implementation sorts the array, so indices may not match original")
    print(f"{'='*60}")
    
    all_passed_nlogn = True
    
    for i, test_case in enumerate(test_cases, 1):
        nums = test_case["nums"].copy()
        target = test_case["target"]
        description = test_case["description"]
        
        try:
            result = solution.twoSumOptimizedNLogN(nums, target)
            
            # For O(n log n), we check if the values at those indices sum to target
            if len(result) == 2:
                sorted_nums = sorted(nums)
                if sorted_nums[result[0]] + sorted_nums[result[1]] == target:
                    print(f"✓ Test {i}: {description}")
                    print(f"  Input: nums = {test_case['nums']}, target = {target}")
                    print(f"  Output: {result} (indices in sorted array)")
                    print(f"  Values: {sorted_nums[result[0]]} + {sorted_nums[result[1]]} = {target}")
                else:
                    print(f"✗ Test {i}: {description}")
                    print(f"  Input: nums = {test_case['nums']}, target = {target}")
                    print(f"  Output: {result}")
                    all_passed_nlogn = False
            else:
                print(f"✗ Test {i}: {description} - Invalid result length")
                all_passed_nlogn = False
                
        except Exception as e:
            print(f"✗ Test {i}: {description} - ERROR: {e}")
            all_passed_nlogn = False
        
        print()
    
    if all_passed_nlogn:
        print(f"🎉 All tests passed for Optimized O(n log n)!")
    else:
        print(f"❌ Some tests failed for Optimized O(n log n)")
    
    # Performance comparison
    print(f"\n{'='*60}")
    print("PERFORMANCE COMPARISON")
    print(f"{'='*60}")
    print("Time Complexity:")
    print("- Brute Force: O(n²)")
    print("- Optimized O(n log n): O(n log n) - but loses original indices")
    print("- Optimized O(n): O(n) - optimal solution")
    print("\nSpace Complexity:")
    print("- Brute Force: O(1)")
    print("- Optimized O(n log n): O(1) - but modifies input array")
    print("- Optimized O(n): O(n) - uses hashmap")


if __name__ == "__main__":
    main()

