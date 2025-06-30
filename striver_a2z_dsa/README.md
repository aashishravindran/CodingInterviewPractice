# Striver A2Z DSA - Problem Explanations

This folder contains solutions and explanations for selected problems from the Striver A2Z DSA Sheet.

---

## 1. 2 Sum Problem ([2SumProblem.py](2SumProblem.py))

### Problem Statement
Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.

### Approaches
- **Brute Force:** Check all pairs (O(n²)).
- **Hash Map:** Store seen numbers and their indices for O(n) lookup.

### Key Insight
- Use a hash map to check if `target - current` exists as you iterate.

---

## 2. Dutch National Flag vs 2 Sum ([DutchNationalFlag_TwoSum_Comparison.md](DutchNationalFlag_TwoSum_Comparison.md))

### Content
- This markdown compares the Dutch National Flag problem (sorting 0s, 1s, 2s) with the 2 Sum problem, highlighting differences in approach and optimality.

---

## 3. Best Time to Buy and Sell Stock ([max_time_to_buy_and_sell_stock.py](max_time_to_buy_and_sell_stock.py))

### Problem Statement
Given an array `prices` where `prices[i]` is the price of a stock on the `i`th day, find the maximum profit you can achieve by buying on one day and selling on another later day. If no profit is possible, return 0.

### Approaches
- **Brute Force:** Try all pairs of days (O(n²)).
- **Optimized (Greedy):** Track the minimum price so far and compute max profit in one pass (O(n)).

### Key Insight
- The best profit at each step depends only on the minimum price seen so far.

---

## 4. Sort 0s and 1s ([sort_zero_and_ones.py](sort_zero_and_ones.py))

### Problem Statement
Given a binary array (only 0s and 1s), sort it in-place so that all 0s come before all 1s.

### Approaches
- **Counting:** Count 0s and 1s, then overwrite the array.
- **Two Pointers:** Swap 0s to the front and 1s to the back in a single pass.

### Key Insight
- Two-pointer approach is optimal for in-place sorting of binary arrays.

---

For detailed code and comments, see the respective files. 