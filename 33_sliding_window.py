# 3. Sliding Window
"""
Foundational Skills
   - Array/string manipulation
   - Loop control
   - Conditional statements
Potential Knowledge Gaps
   - Managing window size (fixed vs. variable)
   - Adjusting the window dynamically (e.g., shrinking or expanding)
"""

# ----------------------------------------------------------------------------------
# 1. Maximum Sum of K Consecutive Elements
"""
Maximum Sum of K Consecutive Elements
Task: Find the maximum sum of any k consecutive elements in an array.
Example: [1, 2, 3, 4], k=2 → 7 (3 + 4)
Why: Introduces fixed-size window sliding, key for Maximum Average Subarray I.
"""

def max_sum_k_consecutive(arr, k):
    if len(arr) < k:
        return None
    window_sum = sum(arr[:k])  # Sum of first window
    max_sum = window_sum
    for i in range(k, len(arr)):
        window_sum = window_sum - arr[i - k] + arr[i]  # Slide window
        max_sum = max(max_sum, window_sum)
    return max_sum

# Test the function
print(max_sum_k_consecutive([1, 2, 3, 4], 2))  # Output: 7 (3 + 4)


# Solution
def max_sum_k_consecutive(arr, k):   # Define the function that takes an array 'arr' and integer 'k'
    """
    Finds the maximum sum of any k consecutive elements.
    
    - Uses a fixed-size sliding window to compute sums efficiently.
    - Time Complexity: O(n), Space Complexity: O(1).
    - Sliding window is intuitive and beginner-friendly for fixed sizes.
    """
    if len(arr) < k:       # Check if the array is shorter than 'k'
        return None        # Return None since we can't form a window of size 'k'
    window_sum = sum(arr[:k])  # Calculate the sum of the first k elements (first window)
    max_sum = window_sum   # Set the initial maximum sum to the first window's sum
    for i in range(k, len(arr)):  # Loop from index k to the end of the array
        window_sum = window_sum - arr[i - k] + arr[i]  # Slide the window: subtract the leftmost element, add the new right element
        max_sum = max(max_sum, window_sum)  # Update max_sum if the current window sum is larger
    return max_sum         # Return the maximum sum found

# Test the function
# print(max_sum_k_consecutive([1, 2, 3, 4], 2))  # Output: 7 (3 + 4)


# ----------------------------------------------------------------------------------
# 2. Count Subarrays with Sum K
"""
Count Subarrays with Sum K
Task: Count subarrays with a given sum.
Example: [1, 2, 3], k=3 → 2 ([1, 2], [3])
Why: Practices maintaining a window with a condition.
"""

def count_subarrays_with_sum(arr, k):
    count = 0
    window_sum = 0
    left = 0
    for right in range(len(arr)):
        window_sum += arr[right]
        while window_sum > k and left <= right:
            window_sum -= arr[left]  # Shrink window
            left += 1
        if window_sum == k:
            count += 1
    return count

# Test the function
print(count_subarrays_with_sum([1, 2, 3], 3))  # Output: 2 ([1, 2], [3])


# Solution
def count_subarrays_with_sum(arr, k):   # Define the function that takes an array 'arr' and integer 'k'
    """
    Counts subarrays with sum equal to k (assuming non-negative numbers).
    
    - Uses a variable-size sliding window to find matching sums.
    - Time Complexity: O(n), Space Complexity: O(1).
    - Simple sliding window approach is beginner-friendly for this case.
    """
    count = 0              # Initialize the count of subarrays with sum equal to k
    window_sum = 0         # Initialize the sum of the current window
    left = 0               # Set the left pointer of the window to the start
    for right in range(len(arr)):  # Loop through the array with the right pointer
        window_sum += arr[right]  # Add the current element to the window sum
        while window_sum > k and left <= right:  # If the sum exceeds k, shrink the window from the left
            window_sum -= arr[left]  # Subtract the leftmost element from the sum
            left += 1            # Move the left pointer one step right
        if window_sum == k:     # If the current window sum equals k
            count += 1          # Increment the count of valid subarrays
    return count               # Return the total number of subarrays found

# Test the function
# print(count_subarrays_with_sum([1, 2, 3], 3))  # Output: 2 ([1, 2], [3])


# ----------------------------------------------------------------------------------
# 3. Longest Substring with At Most K Vowels
"""
Task: Find the longest substring with at most k vowels.
Example: "aeiou", k=2 → "ae"
Why: Introduces dynamic window adjustments.
"""

def longest_substring_with_k_vowels(s, k):
    vowels = set('aeiou')
    max_length = 0
    vowel_count = 0
    left = 0
    for right in range(len(s)):
        if s[right] in vowels:
            vowel_count += 1
        while vowel_count > k and left <= right:
            if s[left] in vowels:
                vowel_count -= 1  # Reduce count when removing a vowel
            left += 1  # Shrink window
        max_length = max(max_length, right - left + 1)
    return max_length

# Test the function
# print(longest_substring_with_k_vowels("aeiou", 2))  # Output: 2


# Solution
def longest_substring_with_k_vowels(s, k):   # Define the function that takes a string 's' and integer 'k'
    """
    Finds the longest substring with at most k vowels.
    
    - Uses a sliding window to track vowel count and adjust window size.
    - Time Complexity: O(n), Space Complexity: O(1).
    - Beginner-friendly with clear window adjustment logic.
    """
    vowels = set('aeiou')  # Create a set of vowels for quick checking
    max_length = 0         # Initialize the maximum length of a valid substring
    vowel_count = 0        # Track the number of vowels in the current window
    left = 0               # Set the left pointer of the window to the start
    for right in range(len(s)):  # Loop through the string with the right pointer
        if s[right] in vowels:   # If the current character is a vowel
            vowel_count += 1     # Increase the vowel count
        while vowel_count > k and left <= right:  # If we have more than k vowels, shrink the window
            if s[left] in vowels:  # If the left character is a vowel
                vowel_count -= 1   # Decrease the vowel count
            left += 1            # Move the left pointer one step right
        max_length = max(max_length, right - left + 1)  # Update max_length with the current window size
    return max_length          # Return the length of the longest valid substring

# Test the function
# print(longest_substring_with_k_vowels("aeiou", 2))  # Output: 2


# ----------------------------------------------------------------------------------
# 4. Minimum Window with All Characters
"""
Task: Find the smallest substring containing all characters of a pattern (e.g., "abc").
Example: "adobecode", pattern "abc" → "adobec"
Why: Builds toward variable-size window problems.
"""


# ----------------------------------------------------------------------------------
# 5. Average of Sliding Window
"""
Average of Sliding Window
Task: Compute the average of all subarrays of size k.
Example: [1, 2, 3, 4], k=2 → [1.5, 2.5, 3.5]
Why: Directly supports Maximum Average Subarray I.
"""

def sliding_window_average(arr, k):
    if len(arr) < k:
        return []
    window_sum = sum(arr[:k])
    averages = [window_sum / k]  # First window average
    for i in range(k, len(arr)):
        window_sum = window_sum - arr[i - k] + arr[i]
        averages.append(window_sum / k)
    return averages

# Test the function
# print(sliding_window_average([1, 2, 3, 4], 2))  # Output: [1.5, 2.5, 3.5]


# Solution
def sliding_window_average(arr, k):   # Define the function that takes an array 'arr' and integer 'k'
    """
    Computes the average of all subarrays of size k.
    
    - Uses a sliding window to compute sums, then averages them.
    - Time Complexity: O(n), Space Complexity: O(n) for result.
    - Simple and beginner-friendly with clear steps.
    """
    if len(arr) < k:       # Check if the array is shorter than 'k'
        return []          # Return an empty list since no subarrays of size k are possible
    window_sum = sum(arr[:k])  # Calculate the sum of the first k elements (first window)
    averages = [window_sum / k]  # Add the average of the first window to the result list
    for i in range(k, len(arr)):  # Loop from index k to the end of the array
        window_sum = window_sum - arr[i - k] + arr[i]  # Slide the window: subtract the leftmost element, add the new right element
        averages.append(window_sum / k)  # Calculate the new average and append it to the list
    return averages        # Return the list of all averages

# Test the function
# print(sliding_window_average([1, 2, 3, 4], 2))  # Output: [1.5, 2.5, 3.5]

