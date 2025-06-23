""" Example 1:

Input: nums = [1,3,4,2,2]
Output: 2
Example 2:

Input: nums = [3,1,3,4,2]
Output: 3
Example 3:

Input: nums = [3,3,3,3,3]
Output: 3
 

Constraints:

1 <= n <= 105
nums.length == n + 1
1 <= nums[i] <= n
All the integers in nums appear only once except for precisely one integer which appears two or more times.
 

Follow up:

How can we prove that at least one duplicate number must exist in nums?
Can you solve the problem in linear runtime complexity? 

Intuition here is that a duplicate number is treated as a cycle

What this means is, at some point we will come back to the same number.

[1,3,4,2,2] -> If we were to treat this as a linked list, we would have a cycle at 2.

1 -> 3 -> 4 -> 2 -> 2
^              |
|              v
2 <- 4 <- 3 <- 1

Therefore we can use floyds tortoise and hare algorithm to find the cycle.

"""

import sys
from typing import List

class Solution:
    """
    Floyd's Tortoise and Hare Algorithm (Cycle Detection) for Finding a Duplicate Number

    This algorithm is used to detect cycles in a sequence (like a linked list) using two pointers:
    - Tortoise (slow): moves one step at a time
    - Hare (fast): moves two steps at a time

    If there is a cycle, the fast pointer will eventually meet the slow pointer inside the cycle.

    Application to Finding a Duplicate Number:
    Given an array of n+1 integers where each integer is between 1 and n (inclusive), there is at least one duplicate.

    Key Insight: Treat the array as a linked list where each index points to the value at that index (i → nums[i]).
    This guarantees a cycle exists due to the pigeonhole principle, and the duplicate number is the entry point of the cycle.

    Algorithm Steps:
    1. Phase 1: Detect the cycle
       - Use two pointers (slow and fast) to find the intersection point inside the cycle.
    2. Phase 2: Find the entrance to the cycle (duplicate number)
       - Reset one pointer to the start and move both one step at a time; the meeting point is the duplicate.

    Example:
    nums = [1,3,4,2,2]
    Linked list: 1 → 3 → 4 → 2 → 2 (cycle at 2)
    The algorithm will detect the cycle and return 2 as the duplicate.
    """
    def findDuplicate(self, nums: List[int]) -> int:
       ### Floyds cycle detection algorithm
       slow,fast = 0,0
       ### This loop simply checks if there is a cycle and we do that by proving that t=if the loop exists then this mus be true 
       while slow != fast:
        slow = nums[slow]
        fast = nums[nums[fast]]
       slow2 = 0


       # Now we need to find the entry point of the cycle which is the duplicate number
       while slow != slow2:
        slow = nums[slow]
        slow2 = nums[slow2]
       return slow

def main():
    # Test case 1
    nums1 = [1, 3, 4, 2, 2]
    expected1 = 2
    print(f"Test 1: nums={nums1}")
    print(f"Expected: {expected1}")
    print(f"Result: {Solution().findDuplicate(nums1)}\n")

    # Test case 2
    nums2 = [3, 1, 3, 4, 2]
    expected2 = 3
    print(f"Test 2: nums={nums2}")
    print(f"Expected: {expected2}")
    print(f"Result: {Solution().findDuplicate(nums2)}\n")

    # Test case 3
    nums3 = [3, 3, 3, 3, 3]
    expected3 = 3
    print(f"Test 3: nums={nums3}")
    print(f"Expected: {expected3}")
    print(f"Result: {Solution().findDuplicate(nums3)}\n")

    # Additional test case
    nums4 = [2, 5, 9, 6, 9, 3, 8, 9, 7, 1]
    expected4 = 9
    print(f"Test 4: nums={nums4}")
    print(f"Expected: {expected4}")
    print(f"Result: {Solution().findDuplicate(nums4)}\n")

if __name__ == "__main__":
    main()