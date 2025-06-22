""" /*
# Problem: Allocate Minimum Number of Pages
Given an array arr[] and an integer k, where arr[i] denotes the number of pages of a book and k denotes total number of students. All the books need to be allocated to k students in contiguous manner, with each student getting at least one book.

The task is to minimize the maximum number of pages allocated to a student. If it is not possible to allocate books to all students, return -

Examples:

Input: arr[] = [12, 34, 67, 90], k = 2
Output: 113
Explanation: Books can be distributed in following ways:

[12] and [34, 67, 90] - The maximum pages assigned to a student is  34 + 67 + 90 = 191.
[12, 34] and [67, 90] - The maximum pages assigned to a student is 67 + 90 = 157.
[12, 34, 67] and [90] - The maximum pages assigned to a student is 12 + 34 + 67 = 113.
The third combination has the minimum pages assigned to a student which is 113.

Input: arr[] = [15, 17, 20], k = 5
Output: -1
Explanation: Since there are more students than total books, it's impossible to allocate a book to each student.

Input: arr[] = [22, 23, 67], k = 1
Output: 112
Explanation: Since there is only 1 student, all books are assigned to that student. So, maximum pages assigned to a student is 22 + 23 + 67 = 112.
*/  """

def is_possible(arr, k, max_pages):
    """
    Check if it's possible to allocate books with maximum 'max_pages' per student
    """
    students_needed = 1
    current_pages = 0
    
    for pages in arr:
        # If a single book has more pages than max_pages, it's impossible
        if pages > max_pages:
            return False
            
        # If adding this book exceeds max_pages, start a new student
        if current_pages + pages > max_pages:
            students_needed += 1
            current_pages = pages
        else:
            current_pages += pages
            
        # If we need more students than available, it's impossible
        if students_needed > k:
            return False
    
    return True

def allocate_minimum_number_pages(arr, k):
    """
    Allocate minimum number of pages using binary search
    
    INTUITION EXPLANATION:
    =====================
    
    Instead of trying all possible book distributions (which would be exponential),
    we use binary search on the answer itself. Here's the key insight:
    
    1. MONOTONICITY PROPERTY:
       - If we can distribute books with max_pages = X, we can also do it with X+1
       - If we cannot distribute with max_pages = X, we cannot do it with X-1
       - This creates a binary searchable pattern: ❌❌❌❌❌✅✅✅✅✅
    
    2. SEARCH SPACE:
       - Left boundary: max(arr) - minimum possible answer (each student needs at least one book)
       - Right boundary: sum(arr) - maximum possible answer (all books to one student)
       - We're looking for the smallest number in this range that works
    
    3. FEASIBILITY CHECK:
       - For each potential answer, we use greedy allocation
       - Keep giving books to current student until limit is reached
       - Start new student when limit is exceeded
       - Check if we can finish with ≤ k students
    
    4. WHY THIS WORKS:
       - Contiguous constraint means we must assign books in order
       - Greedy packing minimizes number of students needed
       - Binary search finds optimal answer without trying all distributions
       - Time complexity: O(n × log(sum - max)) instead of exponential
    
    Args:
        arr: List of page counts for each book
        k: Number of students
    
    Returns:
        Minimum maximum pages any student can get, or -1 if impossible
    """
    # Edge cases
    if not arr or k <= 0:
        return -1
    
    # If more students than books, impossible
    if k > len(arr):
        return -1
    
    # Binary search boundaries
    left = max(arr)  # Minimum possible answer (max single book)
    right = sum(arr)  # Maximum possible answer (all books to one student)
    
    result = -1
    
    while left <= right:
        mid = (left + right) // 2
        
        # Check if it's possible to allocate with 'mid' as max pages
        if is_possible(arr, k, mid):
            result = mid
            right = mid - 1  # Try to find a smaller value
        else:
            left = mid + 1   # Need a larger value
    
    return result

# Test cases
if __name__ == "__main__":
    # Test case 1
    arr1 = [12, 34, 67, 90]
    k1 = 2
    print(f"Test 1: arr={arr1}, k={k1}")
    print(f"Result: {allocate_minimum_number_pages(arr1, k1)}")  # Expected: 113
    print()
    
    # Test case 2
    arr2 = [15, 17, 20]
    k2 = 5
    print(f"Test 2: arr={arr2}, k={k2}")
    print(f"Result: {allocate_minimum_number_pages(arr2, k2)}")  # Expected: -1
    print()
    
    # Test case 3
    arr3 = [22, 23, 67]
    k3 = 1
    print(f"Test 3: arr={arr3}, k={k3}")
    print(f"Result: {allocate_minimum_number_pages(arr3, k3)}")  # Expected: 112
    print()
    
    # Additional test case
    arr4 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    k4 = 3
    print(f"Test 4: arr={arr4}, k={k4}")
    print(f"Result: {allocate_minimum_number_pages(arr4, k4)}")  # Expected: 17
