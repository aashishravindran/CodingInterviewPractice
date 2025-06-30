# Others - Coding Interview Problems

This folder contains solutions and explanations for selected coding interview problems.

---

## 1. Happy Number ([happy_number.py](happy_number.py))

### Problem Statement
A **happy number** is a number defined by the following process:
- Starting with any positive integer, replace the number by the sum of the squares of its digits.
- Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
- Those numbers for which this process ends in 1 are happy.

**Return true if n is a happy number, and false if not.**

### Approaches

#### 1. Brute Force (Using a Set)
- Track all numbers seen so far in a set.
- If a number repeats, a cycle exists (not happy).
- If the process reaches 1, the number is happy.
- **Time Complexity:** O(log n) per iteration, but can loop for many steps in worst case.

#### 2. Floyd's Tortoise and Hare (Cycle Detection)
- Use two pointers (slow and fast):
  - Slow moves one step (sum of squares once), fast moves two steps (sum of squares twice).
  - If there is a cycle (not happy), slow and fast will meet at a number not equal to 1.
  - If the number is happy, fast (and slow) will reach 1.
- **Space Complexity:** O(1) (no extra set needed).

### Key Insight
- The process either ends at 1 (happy) or falls into a cycle (not happy).
- Cycle detection can be done efficiently with two pointers.

---

## 2. Find Minimum in Rotated Sorted Array ([find_minimum_in_rotated_sorted.py](find_minimum_in_rotated_sorted.py))

### Problem Statement
Given a rotated sorted array (no duplicates), find the minimum element.

**Example:**
- Input: `[3,4,5,1,2]`
- Output: `1`

### Approach

#### Binary Search
- The minimum element is the only element whose previous is greater than itself.
- Use binary search to find the inflection point:
  - If `mid` element is greater than the rightmost, the minimum is to the right.
  - Otherwise, the minimum is to the left (or at mid).
- **Time Complexity:** O(log n)

### Key Insight
- The rotated array can be split into two sorted subarrays; the minimum is at the rotation point.

---

Feel free to check the code files for detailed implementations and comments. 