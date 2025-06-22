# Allocate Minimum Number of Pages

## Problem Description

Given an array `arr[]` and an integer `k`, where `arr[i]` denotes the number of pages of a book and `k` denotes the total number of students. All the books need to be allocated to `k` students in a **contiguous manner**, with each student getting at least one book.

**Goal**: Minimize the maximum number of pages allocated to any student.

**Return**: The minimum maximum pages, or `-1` if allocation is impossible.

## Examples

### Example 1
```
Input: arr[] = [12, 34, 67, 90], k = 2
Output: 113

Explanation: Books can be distributed in following ways:
- [12] and [34, 67, 90] → max = 34 + 67 + 90 = 191
- [12, 34] and [67, 90] → max = 67 + 90 = 157  
- [12, 34, 67] and [90] → max = 12 + 34 + 67 = 113 ← Optimal

The third combination has the minimum maximum pages: 113
```

### Example 2
```
Input: arr[] = [15, 17, 20], k = 5
Output: -1

Explanation: Since there are more students (5) than total books (3), 
it's impossible to allocate a book to each student.
```

### Example 3
```
Input: arr[] = [22, 23, 67], k = 1
Output: 112

Explanation: Since there is only 1 student, all books are assigned to that student.
Maximum pages = 22 + 23 + 67 = 112
```

## Solution Approach

### Key Insight: Binary Search on Answer

Instead of trying all possible book distributions (which would be exponential), we use **binary search on the answer itself**.

### Why Binary Search Works

#### 1. Monotonicity Property
- If we can distribute books with `max_pages = X`, we can also do it with `X+1`
- If we cannot distribute with `max_pages = X`, we cannot do it with `X-1`
- This creates a binary searchable pattern: `❌❌❌❌❌✅✅✅✅✅`

#### 2. Search Space
- **Left boundary**: `max(arr)` - minimum possible answer (each student needs at least one book)
- **Right boundary**: `sum(arr)` - maximum possible answer (all books to one student)
- We're looking for the smallest number in this range that works

#### 3. Feasibility Check
For each potential answer, we use **greedy allocation**:
- Keep giving books to current student until limit is reached
- Start new student when limit is exceeded
- Check if we can finish with ≤ k students

### Algorithm Steps

1. **Edge Cases**: Check if allocation is impossible
2. **Binary Search Setup**: Set search boundaries
3. **Binary Search Loop**: 
   - Try middle value
   - If feasible, search left half (try smaller)
   - If not feasible, search right half (try larger)
4. **Feasibility Function**: Greedy allocation with given limit

## Detailed Walkthrough

### Example Walkthrough: arr = [12, 34, 67, 90], k = 2

**Step 1: Determine Search Space**
- Left boundary = max(arr) = 90
- Right boundary = sum(arr) = 12 + 34 + 67 + 90 = 203
- Search space: [90, 203]

**Step 2: Binary Search Execution**

| Iteration | left | right | mid | is_possible(mid) | Action |
|-----------|------|-------|-----|------------------|---------|
| 1 | 90 | 203 | 146 | ✅ | Search left (try smaller) |
| 2 | 90 | 145 | 117 | ✅ | Search left (try smaller) |
| 3 | 90 | 116 | 103 | ❌ | Search right (need larger) |
| 4 | 104 | 116 | 110 | ❌ | Search right (need larger) |
| 5 | 111 | 116 | 113 | ✅ | Search left (try smaller) |
| 6 | 111 | 112 | 111 | ❌ | Search right (need larger) |
| 7 | 112 | 112 | 112 | ❌ | Search right (need larger) |
| 8 | 113 | 112 | - | - | Exit loop |

**Result**: 113 (found in iteration 5)

**Step 3: Verify Feasibility for mid = 113**

```
Student 1: [12, 34, 67] → 12 + 34 + 67 = 113 ✅
Student 2: [90] → 90 ✅
Total students needed: 2 ✅
```

### Example Walkthrough: arr = [1, 2, 3, 4, 5, 6, 7, 8, 9], k = 3

**Step 1: Determine Search Space**
- Left boundary = max(arr) = 9
- Right boundary = sum(arr) = 45
- Search space: [9, 45]

**Step 2: Binary Search Execution**

| Iteration | left | right | mid | is_possible(mid) | Action |
|-----------|------|-------|-----|------------------|---------|
| 1 | 9 | 45 | 27 | ✅ | Search left (try smaller) |
| 2 | 9 | 26 | 17 | ✅ | Search left (try smaller) |
| 3 | 9 | 16 | 12 | ❌ | Search right (need larger) |
| 4 | 13 | 16 | 14 | ❌ | Search right (need larger) |
| 5 | 15 | 16 | 15 | ❌ | Search right (need larger) |
| 6 | 16 | 16 | 16 | ❌ | Search right (need larger) |
| 7 | 17 | 16 | - | - | Exit loop |

**Result**: 17 (found in iteration 2)

**Step 3: Verify Feasibility for mid = 17**

```
Student 1: [1, 2, 3, 4, 5] → 1 + 2 + 3 + 4 + 5 = 15 ✅
Student 2: [6, 7] → 6 + 7 = 13 ✅
Student 3: [8, 9] → 8 + 9 = 17 ✅
Total students needed: 3 ✅
```

### Example Walkthrough: arr = [15, 17, 20], k = 5

**Step 1: Edge Case Check**
- Number of books (3) < Number of students (5)
- **Result**: -1 (impossible to allocate)

**Why**: Each student must get at least one book, but we only have 3 books for 5 students.

## Time & Space Complexity

- **Time Complexity**: O(n × log(sum - max))
  - Binary search: O(log(sum - max))
  - Feasibility check: O(n)
- **Space Complexity**: O(1)

## Code Implementation

The solution is implemented in `allocate-minimum-number-pages.py` with:
- `allocate_minimum_number_pages()`: Main function with binary search
- `is_possible()`: Feasibility check function
- Comprehensive test cases

## Intuition Behind the Solution

### Why Not Brute Force?
If we tried to enumerate all possible distributions:
- For n books and k students, we'd need to try all ways to split n-1 positions into k-1 groups
- This would be **exponentially complex**

### The "Aha!" Moment
The breakthrough is realizing that:
1. **We don't need to find the exact distribution** - we just need to know if one exists
2. **The feasibility check is simple** - just greedy allocation
3. **Binary search finds the optimal answer** without trying all possibilities

### Real-World Analogy
Think of it like **packing boxes**:
- You have items of different weights
- You need to pack them into k boxes
- You want to minimize the heaviest box
- You can't split items (contiguous constraint)

**The approach**: 
- Guess a maximum weight limit
- Try to pack everything within that limit
- If you need more boxes than available, increase the limit
- If you succeed, try a smaller limit

## Similar Problems

This pattern applies to many optimization problems:
- Ship capacity optimization
- Load balancing
- Resource allocation
- Scheduling problems
- Aggressive cows (binary search on answer)

## Key Takeaways

1. **Binary search on answer** is powerful for optimization problems
2. **Monotonicity** makes binary search possible
3. **Greedy feasibility check** is often simpler than finding optimal distribution
4. **Contiguous constraint** makes the problem more tractable
5. **Time complexity** improves from exponential to logarithmic

## Running the Code

```bash
python3 allocate-minimum-number-pages.py
```

This will run all test cases and show the results.

## Test Cases Included

1. `[12, 34, 67, 90], k=2` → 113
2. `[15, 17, 20], k=5` → -1
3. `[22, 23, 67], k=1` → 112
4. `[1, 2, 3, 4, 5, 6, 7, 8, 9], k=3` → 17 