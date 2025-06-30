# 202. Happy Number
# Solved
# Easy
# Topics
# conpanies icon
# Companies
# Write an algorithm to determine if a number n is happy.

# A happy number is a number defined by the following process:

# Starting with any positive integer, replace the number by the sum of the squares of its digits.
# Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
# Those numbers for which this process ends in 1 are happy.
# Return true if n is a happy number, and false if not.

class Solution:
    """
    The Brute force solution is to use a set , 
    If that number is already in the set then we return false 
    i.e there is CYCLE
    """
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = self.sum_of_squares(n)

        ### In the end all we need to check is if the number was 1 :P    
        return n == 1 
    ### Lol this one liner beats the more ardous way to compute sum of squares 
    ### This function is also given below 
    def sum_of_squares(self, n: int) -> int:
        return sum(int(digit)**2 for digit in str(n))

    ### Proper implementation of sum of squares   
    def proper_sum_of_squares(self, n: int) -> int:
        sum = 0
        while n != 0:
            rem = n % 10
            sum+= rem*rem
            n = n // 10
        return sum
    
    def is_happy_floyds_tortoise_and_hare(self, n: int) -> bool:
     """
     Use two pointes slow and fast, 
     slow moves one step at a time, fast moves two steps at a time
     if there is a cycle, slow and fast will meet at some point and they wont be equal to 1
     if there is no cycle, fast will reach 1 first and slow will be equal to 1
     """
     slow = self.sum_of_squares(n)
     fast = self.sum_of_squares(self.sum_of_squares(n))

     while slow != fast:
         slow = self.sum_of_squares(slow)
         fast = self.sum_of_squares(self.sum_of_squares(fast))

     return slow == 1
    
def main():
    sol = Solution()
    print(sol.is_happy_floyds_tortoise_and_hare(19))

if __name__ == "__main__":
    main()