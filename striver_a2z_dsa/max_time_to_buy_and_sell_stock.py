# 121. Best Time to Buy and Sell Stock

from typing import List

# # Example 1:

# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
# Example 2:

# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.
 

# Constraints:

# 1 <= prices.length <= 105
# 0 <= prices[i] <= 104

## Problem Description
# You are given an array `prices` where `prices[i]` is the price of a given stock on the `i`th day. You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock. Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

# ## Intuition and Why the Solution Works

# ### Key Insight: Track Minimum Price and Maximum Profit
# The core idea is to keep track of the minimum price seen so far and calculate the potential profit if we sell at the current price. We don't need to store all historical prices - we only need to remember the minimum price encountered.

# ### Why This Works:
# 1. **Single Pass**: We only need to traverse the array once
# 2. **Greedy Approach**: At each step, we either:
#    - Update the minimum price if we find a lower price
#    - Calculate potential profit if current price is higher than minimum
# 3. **Optimal Substructure**: The best profit up to day i depends only on the minimum price seen before day i

# ### Example Walkthrough: [7,1,5,3,6,4]
# - Day 0: min_price = 7, max_profit = 0
# - Day 1: min_price = 1 (update), max_profit = 0
# - Day 2: min_price = 1, max_profit = max(0, 5-1) = 4
# - Day 3: min_price = 1, max_profit = max(4, 3-1) = 4
# - Day 4: min_price = 1, max_profit = max(4, 6-1) = 5
# - Day 5: min_price = 1, max_profit = max(5, 4-1) = 5

## Brute Force Solution (O(n²))

class Solution:
    
    # Brute Force Solution - Time Complexity: O(n²)
    def maxProfitBruteForce(self, prices: List[int]) -> int:
        """
        Brute force approach: Check all possible buy-sell combinations
        Time Complexity: O(n²)
        Space Complexity: O(1)
        """
        max_profit = 0
        n = len(prices)
        
        for i in range(n):
            for j in range(i + 1, n):
                profit = prices[j] - prices[i]
                max_profit = max(max_profit, profit)
        
        return max_profit

    # Optimized Solution - Time Complexity: O(n)
    def maxProfit(self, prices: List[int]) -> int:
        """
        Optimized approach: Track minimum price and calculate potential profit
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        if not prices:
            return 0
            
        min_price = prices[0]
        max_profit = 0
        
        for price in prices[1:]:
            # Update minimum price if we find a lower price
            min_price = min(min_price, price)
            # Calculate potential profit if we sell at current price
            max_profit = max(max_profit, price - min_price)
        
        return max_profit


# Unit Tests
import unittest

class TestMaxProfit(unittest.TestCase):
    
    def setUp(self):
        self.solution = Solution()
    
    def test_example_1(self):
        """Test Example 1: [7,1,5,3,6,4] -> 5"""
        prices = [7, 1, 5, 3, 6, 4]
        self.assertEqual(self.solution.maxProfitBruteForce(prices), 5)
        self.assertEqual(self.solution.maxProfit(prices), 5)
    
    def test_example_2(self):
        """Test Example 2: [7,6,4,3,1] -> 0"""
        prices = [7, 6, 4, 3, 1]
        self.assertEqual(self.solution.maxProfitBruteForce(prices), 0)
        self.assertEqual(self.solution.maxProfit(prices), 0)
    
    def test_single_element(self):
        """Test single element array"""
        prices = [5]
        self.assertEqual(self.solution.maxProfitBruteForce(prices), 0)
        self.assertEqual(self.solution.maxProfit(prices), 0)
    
    def test_two_elements_increasing(self):
        """Test two elements with increasing prices"""
        prices = [1, 5]
        self.assertEqual(self.solution.maxProfitBruteForce(prices), 4)
        self.assertEqual(self.solution.maxProfit(prices), 4)
    
    def test_two_elements_decreasing(self):
        """Test two elements with decreasing prices"""
        prices = [5, 1]
        self.assertEqual(self.solution.maxProfitBruteForce(prices), 0)
        self.assertEqual(self.solution.maxProfit(prices), 0)
    
    def test_all_same_prices(self):
        """Test array with all same prices"""
        prices = [3, 3, 3, 3, 3]
        self.assertEqual(self.solution.maxProfitBruteForce(prices), 0)
        self.assertEqual(self.solution.maxProfit(prices), 0)
    
    def test_increasing_prices(self):
        """Test strictly increasing prices"""
        prices = [1, 2, 3, 4, 5]
        self.assertEqual(self.solution.maxProfitBruteForce(prices), 4)
        self.assertEqual(self.solution.maxProfit(prices), 4)
    
    def test_decreasing_prices(self):
        """Test strictly decreasing prices"""
        prices = [5, 4, 3, 2, 1]
        self.assertEqual(self.solution.maxProfitBruteForce(prices), 0)
        self.assertEqual(self.solution.maxProfit(prices), 0)
    
    def test_peak_in_middle(self):
        """Test with peak in the middle"""
        prices = [1, 2, 10, 3, 4]
        self.assertEqual(self.solution.maxProfitBruteForce(prices), 9)
        self.assertEqual(self.solution.maxProfit(prices), 9)
    
    def test_valley_in_middle(self):
        """Test with valley in the middle"""
        prices = [10, 9, 1, 8, 7]
        self.assertEqual(self.solution.maxProfitBruteForce(prices), 7)
        self.assertEqual(self.solution.maxProfit(prices), 7)
    
    def test_empty_array(self):
        """Test empty array"""
        prices = []
        self.assertEqual(self.solution.maxProfitBruteForce(prices), 0)
        self.assertEqual(self.solution.maxProfit(prices), 0)
    
    def test_large_profit(self):
        """Test with large profit potential"""
        prices = [1, 1000]
        self.assertEqual(self.solution.maxProfitBruteForce(prices), 999)
        self.assertEqual(self.solution.maxProfit(prices), 999)
    
    def test_negative_prices(self):
        """Test with negative prices (edge case)"""
        prices = [-5, -3, -1, -10, -2]
        self.assertEqual(self.solution.maxProfitBruteForce(prices), 8)
        self.assertEqual(self.solution.maxProfit(prices), 8)


if __name__ == "__main__":
    # Run unit tests
    unittest.main(verbosity=2)
    
    # Example usage
    solution = Solution()
    
    # Test cases
    test_cases = [
        [7, 1, 5, 3, 6, 4],  # Expected: 5
        [7, 6, 4, 3, 1],     # Expected: 0
        [1, 2, 3, 4, 5],     # Expected: 4
        [5, 4, 3, 2, 1],     # Expected: 0
        [1, 1000],           # Expected: 999
    ]
    
    print("Testing both solutions:")
    for i, prices in enumerate(test_cases):
        brute_force_result = solution.maxProfitBruteForce(prices)
        optimized_result = solution.maxProfit(prices)
        print(f"Test {i+1}: {prices}")
        print(f"  Brute Force: {brute_force_result}")
        print(f"  Optimized:   {optimized_result}")
        print(f"  Match:       {brute_force_result == optimized_result}")
        print()
        