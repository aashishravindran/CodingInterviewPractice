from typing import List

class Solution:
    def sortZeroAndOnes(self, nums: List[int]) -> List[int]:
        """
        Dutch National Flag Algorithm for sorting an array containing only 0, 1, and 2.
        
        Given an array nums consisting of only 0, 1, or 2. Sort the array in non-decreasing order. 
        The sorting must be done in-place, without making a copy of the original array.
        
        We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
        You must solve this problem without using the library's sort function.      

        Example 1:
        Input: nums = [2,0,2,1,1,0]
        Output: [0,0,1,1,2,2]
        
        Example 2:
        Input: nums = [2,0,1]
        Output: [0,1,2]

        Constraints:
        n == nums.length
        1 <= n <= 300
        nums[i] is either 0, 1, or 2.
        """
        # Dutch National Flag Algorithm
        low, mid, high = 0, 0, len(nums) - 1
        
        while mid <= high:
            if nums[mid] == 0:
                # Swap with low pointer and move both pointers
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                # Just move mid pointer (1s stay in place)
                mid += 1
            else:  # nums[mid] == 2
                # Swap with high pointer and move high pointer left
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1
        
        return nums

    def dutchNationalFlagExplanation(self):
        
        """
        DETAILED EXPLANATION OF THE DUTCH NATIONAL FLAG ALGORITHM:
        
        The Dutch National Flag algorithm is a three-way partitioning algorithm that sorts an array 
        containing only three distinct values (0, 1, 2) in a single pass using three pointers.
        
        HOW IT WORKS:
        =============
        
        1. THREE POINTERS:
           - low: Points to the end of the 0s section (exclusive)
           - mid: Current element being examined
           - high: Points to the beginning of the 2s section (exclusive)
        
        2. INVARIANTS (what we maintain throughout the algorithm):
           - All elements before 'low' are 0s
           - All elements between 'low' and 'mid' are 1s
           - All elements after 'high' are 2s
           - Elements between 'mid' and 'high' are unclassified
        
        3. ALGORITHM STEPS:
           While mid <= high:
           - If nums[mid] == 0: Swap with low, increment both low and mid
           - If nums[mid] == 1: Just increment mid (1s stay in place)
           - If nums[mid] == 2: Swap with high, decrement high

        BY ENSURING YOU SWAP 0 AND 2, you are automatically sorting 1's into its own place 
        
        STEP-BY-STEP WALKTHROUGH:
        =========================
        
        Example: nums = [2, 0, 2, 1, 1, 0]
        
        Initial state: [2, 0, 2, 1, 1, 0]
                       l  m           h
                       ↑  ↑           ↑
        
        Step 1: nums[mid] = 0
        - Swap nums[low] and nums[mid]: [0, 2, 2, 1, 1, 0]
        - Increment low and mid: [0, 2, 2, 1, 1, 0]
                                  l  m         h
                                  ↑  ↑         ↑
        
        Step 2: nums[mid] = 2
        - Swap nums[mid] and nums[high]: [0, 0, 2, 1, 1, 2]
        - Decrement high: [0, 0, 2, 1, 1, 2]
                           l  m       h
                           ↑  ↑       ↑
        
        Step 3: nums[mid] = 2
        - Swap nums[mid] and nums[high]: [0, 0, 1, 1, 2, 2]
        - Decrement high: [0, 0, 1, 1, 2, 2]
                           l  m     h
                           ↑  ↑     ↑
        
        Step 4: nums[mid] = 1
        - Just increment mid: [0, 0, 1, 1, 2, 2]
                                l     m   h
                                ↑     ↑   ↑
        
        Step 5: nums[mid] = 1
        - Just increment mid: [0, 0, 1, 1, 2, 2]
                                l       m h
                                ↑       ↑ ↑
        
        Step 6: nums[mid] = 2
        - Swap nums[mid] and nums[high]: [0, 0, 1, 1, 2, 2]
        - Decrement high: [0, 0, 1, 1, 2, 2]
                                l     h m
                                ↑     ↑ ↑
        
        Now mid > high, so we stop. Result: [0, 0, 1, 1, 2, 2]
        
        WHY THIS ALGORITHM WORKS:
        =========================
        
        1. CORRECTNESS:
           - 0s are always moved to the left of 'low'
           - 2s are always moved to the right of 'high'
           - 1s naturally end up in the middle
           - The algorithm processes each element at most twice (once when mid points to it, 
             and possibly once more if it gets swapped)
        
        2. EFFICIENCY:
           - Time Complexity: O(n) - single pass through the array
           - Space Complexity: O(1) - in-place sorting
           - Each element is swapped at most once
        
        3. INVARIANT MAINTENANCE:
           - The three sections (0s, 1s, 2s) are maintained throughout
           - The unclassified region shrinks with each iteration
           - When mid > high, all elements are classified
        
        APPLICATIONS TO TWO SUM PROBLEM:
        ===============================
        
        While the Dutch National Flag algorithm is designed for three-way partitioning, 
        its core concept of using multiple pointers can be adapted for the Two Sum problem:
        
        1. TWO POINTERS APPROACH (for sorted arrays):
           - Similar to the O(n log n) solution we implemented
           - Use low and high pointers to find pairs
           - Move pointers based on comparison with target
        
        2. HASHMAP APPROACH (current O(n) solution):
           - While not directly related, the concept of "partitioning" the search space
           - We partition elements into "seen" and "unseen" categories
           - This is conceptually similar to the three-way partitioning idea
        
        3. VARIATIONS:
           - Three Sum problem: Could use three pointers
           - Four Sum problem: Could use four pointers
           - The Dutch National Flag shows how multiple pointers can efficiently 
             partition and search through arrays
        
        REAL-WORLD ANALOGY:
        ===================
        
        Think of it like sorting colored balls:
        - You have red (0), white (1), and blue (2) balls mixed together
        - You want to arrange them in order: red, white, blue
        - You use three containers and three hands:
          * Left hand (low): collects red balls
          * Middle hand (mid): examines current ball
          * Right hand (high): collects blue balls
        - White balls naturally end up in the middle
        
        This is why it's called the "Dutch National Flag" algorithm - 
        it sorts elements into three sections like the three stripes 
        of the Dutch flag (red, white, blue).
        """
        low = 0
        mid = 0
        high = len(nums) - 1
        
        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1

        return nums


def main():
    """
    Test the Dutch National Flag algorithm
    """
    solution = Solution()
    
    test_cases = [
        {
            "nums": [2, 0, 2, 1, 1, 0],
            "expected": [0, 0, 1, 1, 2, 2],
            "description": "Example 1: Mixed array"
        },
        {
            "nums": [2, 0, 1],
            "expected": [0, 1, 2],
            "description": "Example 2: Small array"
        },
        {
            "nums": [0, 0, 0],
            "expected": [0, 0, 0],
            "description": "All zeros"
        },
        {
            "nums": [1, 1, 1],
            "expected": [1, 1, 1],
            "description": "All ones"
        },
        {
            "nums": [2, 2, 2],
            "expected": [2, 2, 2],
            "description": "All twos"
        },
        {
            "nums": [1, 0, 2, 1, 0, 2, 1, 0],
            "expected": [0, 0, 0, 1, 1, 1, 2, 2],
            "description": "Complex pattern"
        }
    ]
    
    print("DUTCH NATIONAL FLAG ALGORITHM TESTING")
    print("=" * 50)
    
    for i, test_case in enumerate(test_cases, 1):
        nums = test_case["nums"].copy()
        expected = test_case["expected"]
        description = test_case["description"]
        
        result = solution.sortZeroAndOnes(nums)
        
        if result == expected:
            print(f"✓ Test {i}: {description}")
            print(f"  Input: {test_case['nums']}")
            print(f"  Output: {result}")
        else:
            print(f"✗ Test {i}: {description}")
            print(f"  Input: {test_case['nums']}")
            print(f"  Output: {result}")
            print(f"  Expected: {expected}")
        print()


if __name__ == "__main__":
    main()        