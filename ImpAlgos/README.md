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
