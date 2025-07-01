# _You are given a 0-indexed integer array nums of even length consisting of an equal number of positive and negative integers.

# You should return the array of nums such that the the array follows the given conditions:

# Every consecutive pair of integers have opposite signs.
# For all integers with the same sign, the order in which they were present in nums is preserved.
# The rearranged array begins with a positive integer.
# Return the modified array after rearranging the elements to satisfy the aforementioned conditions.

 

# Example 1:

# Input: nums = [3,1,-2,-5,2,-4]
# Output: [3,-2,1,-5,2,-4]
# Explanation:
# The positive integers in nums are [3,1,2]. The negative integers are [-2,-5,-4].
# The only possible way to rearrange them such that they satisfy all conditions is [3,-2,1,-5,2,-4].
# Other ways such as [1,-2,2,-5,3,-4], [3,1,2,-2,-5,-4], [-2,3,-5,1,-4,2] are incorrect because they do not satisfy one or more conditions.  
# Example 2:

# Input: nums = [-1,1]
# Output: [1,-1]
# Explanation:
# 1 is the only positive integer and -1 the only negative integer in nums.
# So nums is rearranged to [1,-1].
 

# Constraints:

# 2 <= nums.length <= 2 * 105
# nums.length is even
# 1 <= |nums[i]| <= 105
# nums consists of equal number of positive and negative integers.
 

# It is not required to do the modifications in-place.

from typing import List

class Solution:
    """
    Rearrange Array Elements by Sign
    --------------------------------
    Given an array with an equal number of positive and negative integers, rearrange it so that:
      - Every consecutive pair of integers have opposite signs.
      - The order of positive and negative numbers is preserved.
      - The array starts with a positive integer.

    Approach:
      - Use a result array of the same length as input.
      - Place positive numbers at even indices (0, 2, 4, ...).
      - Place negative numbers at odd indices (1, 3, 5, ...).
      - Iterate through the input, placing each number in the next available even or odd index, preserving order.

    Why this works:
      - The array is guaranteed to have equal numbers of positives and negatives.
      - By alternating placement starting with a positive at index 0, we ensure the required sign alternation and order preservation.

    Example:
      nums = [3,1,-2,-5,2,-4]
      Positives: 3, 1, 2 → indices 0, 2, 4
      Negatives: -2, -5, -4 → indices 1, 3, 5
      Result: [3, -2, 1, -5, 2, -4]

    Complexity:
      - Time: O(n)
      - Space: O(n)
    """
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        res = [0]*len(nums)

        even_numeber = 0 
        odd_number = 1 

        for idx, element in enumerate(nums):
            if element > 0:
                res[even_numeber] = element
                even_numeber+=2
            else:
                res[odd_number] = element 
                odd_number +=2 
        return res  


    ## If positive is not equal to negative   
    def rearrangeArray_2(self, nums: List[int]) -> List[int]:
        positives = [x for x in nums if x > 0]
        negatives = [x for x in nums if x < 0]
        res = []
        i = j = 0
        # Start with positive if available, else negative
        turn_positive = True if positives else False

        while i < len(positives) and j < len(negatives):
            if turn_positive:
                res.append(positives[i])
                i += 1
            else:
                res.append(negatives[j])
                j += 1
            # Toggle the turn_positive flag pick one from negative and one from positive
            turn_positive = not turn_positive

        # Append the rest
        res.extend(positives[i:])
        res.extend(negatives[j:])
        return res


def main():
    sol = Solution()
    print(sol.rearrangeArray([3,1,-2,-5,2,-4]))

if __name__ == "__main__":
    main()