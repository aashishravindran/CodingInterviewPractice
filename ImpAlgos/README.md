# Floyd's Tortoise and Hare Algorithm (Cycle Detection) - Find Duplicate Number

## Problem Statement
Given an array of n+1 integers where each integer is between 1 and n (inclusive), there is at least one duplicate. The task is to find the duplicate number without modifying the array and using only constant extra space.

## Algorithm Intuition
Floyd's Tortoise and Hare algorithm is a classic cycle detection technique. By treating the array as a linked list (where each index points to the value at that index), the presence of a duplicate guarantees a cycle. The entry point of the cycle is the duplicate number.

## How the Algorithm Works
1. **Phase 1: Detect the Cycle**
   - Use two pointers: Tortoise (moves one step) and Hare (moves two steps).
   - Move both pointers until they meet inside the cycle.
2. **Phase 2: Find the Entrance to the Cycle (Duplicate Number)**
   - Reset one pointer to the start of the array.
   - Move both pointers one step at a time; the meeting point is the duplicate number.

## Example
Input: `[1, 3, 4, 2, 2]`

Visualized as a linked list:
1 → 3 → 4 → 2 → 2 (cycle at 2)

The algorithm will detect the cycle and return 2 as the duplicate.

## Python Implementation
See `floyds_tortoise_and_hare.py` for the implementation:


## References
- [Floyd's Tortoise and Hare (Cycle Detection) - Wikipedia](https://en.wikipedia.org/wiki/Cycle_detection)
- LeetCode 287. Find the Duplicate Number

---

# Kadane's Algorithm (Maximum Subarray Sum)

## Problem Statement
Given an integer array `nums`, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

## Algorithm Intuition
Kadane's Algorithm is a dynamic programming approach that efficiently finds the maximum sum of a contiguous subarray in O(n) time. The key insight is that if the running sum becomes negative, it is better to start a new subarray from the next element.

## How the Algorithm Works
1. Initialize two variables:
   - `max_sum`: the maximum sum found so far (start with the first element)
   - `current_sum`: the sum of the current subarray (start at 0)
2. Iterate through the array:
   - Add the current element to `current_sum`.
   - If `current_sum` is greater than `max_sum`, update `max_sum`.
   - If `current_sum` drops below 0, reset it to 0 (start a new subarray from the next index).
3. At the end, `max_sum` contains the largest sum.

## Example
Input: `[-2, 1, -3, 4, -1, 2, 1, -5, 4]`

Step-by-step:
| Index | Num | Current Sum | Max Sum | Action                |
|-------|-----|-------------|---------|-----------------------|
| 0     | -2  | -2          | -2      | Start, set both       |
| 1     | 1   | 1           | 1       | Reset, new max        |
| 2     | -3  | -2          | 1       | Reset                 |
| 3     | 4   | 4           | 4       | Reset, new max        |
| 4     | -1  | 3           | 4       | Continue              |
| 5     | 2   | 5           | 5       | New max               |
| 6     | 1   | 6           | 6       | New max               |
| 7     | -5  | 1           | 6       | Continue              |
| 8     | 4   | 5           | 6       | Continue              |

The largest sum is 6, from subarray `[4, -1, 2, 1]`.

## Python Implementation
See `kadanes_algorithm.py` for the implementation, including code to print the subarray that gives the maximum sum.

## References
- [Kadane's Algorithm - Wikipedia](https://en.wikipedia.org/wiki/Maximum_subarray_problem)
- LeetCode 53. Maximum Subarray
