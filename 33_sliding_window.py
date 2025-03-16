# 3. Sliding Window


# 1. Maximum Sum of K Consecutive Elements
"""
Maximum Sum of K Consecutive Elements
Task: Find the maximum sum of any k consecutive elements in an array.
Example: [1, 2, 3, 4], k=2 → 7 (3 + 4)
Why: Introduces fixed-size window sliding, key for Maximum Average Subarray I.
"""

# Solution
def max_sum_k_consecutive(arr, k):
    """
    Finds the maximum sum of any k consecutive elements.
    
    - Uses a fixed-size sliding window to compute sums efficiently.
    - Time Complexity: O(n), Space Complexity: O(1).
    - Sliding window is intuitive and beginner-friendly for fixed sizes.
    """
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


# ----------------------------------------------------------------------------------
# 2. Count Subarrays with Sum K

"""
Count Subarrays with Sum K
Task: Count subarrays with a given sum.
Example: [1, 2, 3], k=3 → 2 ([1, 2], [3])
Why: Practices maintaining a window with a condition.
"""

def count_subarrays_with_sum(arr, k):
    """
    Counts subarrays with sum equal to k (assuming non-negative numbers).
    
    - Uses a variable-size sliding window to find matching sums.
    - Time Complexity: O(n), Space Complexity: O(1).
    - Simple sliding window approach is beginner-friendly for this case.
    """
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


# ----------------------------------------------------------------------------------
# 3. Longest Substring with At Most K Vowels

"""
Task: Find the longest substring with at most k vowels.
Example: "aeiou", k=2 → "ae"
Why: Introduces dynamic window adjustments.
"""

def longest_substring_with_k_vowels(s, k):
    """
    Finds the longest substring with at most k vowels.
    
    - Uses a sliding window to track vowel count and adjust window size.
    - Time Complexity: O(n), Space Complexity: O(1).
    - Beginner-friendly with clear window adjustment logic.
    """
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
print(longest_substring_with_k_vowels("aeiou", 2))  # Output: 2


# ----------------------------------------------------------------------------------
# 4. Minimum Window with All Characters

"""
Task: Find the smallest substring containing all characters of a pattern (e.g., "abc").
Example: "adobecode", pattern "abc" → "adobec"
Why: Builds toward variable-size window problems.
"""


def min_window_with_all_chars(s, pattern):
    """
    Finds the smallest substring containing all characters of the pattern.
    
    - Uses a sliding window with a frequency map for efficiency.
    - Time Complexity: O(n), Space Complexity: O(k) where k is pattern length.
    - Chosen over brute force for efficiency, with comments to aid understanding.
    """
    from collections import Counter
    pattern_count = Counter(pattern)  # Frequency of each pattern char
    required = len(pattern_count)     # Number of unique chars to match
    formed = 0                        # Number of chars fully matched
    left, right = 0, 0
    window_counts = {}                # Frequency in current window
    min_length = float('inf')
    min_window = ""

    while right < len(s):
        char = s[right]
        window_counts[char] = window_counts.get(char, 0) + 1
        if char in pattern_count and window_counts[char] == pattern_count[char]:
            formed += 1  # A character requirement is met
        while left <= right and formed == required:
            if right - left + 1 < min_length:
                min_length = right - left + 1
                min_window = s[left:right + 1]
            char = s[left]
            window_counts[char] -= 1
            if char in pattern_count and window_counts[char] < pattern_count[char]:
                formed -= 1  # A requirement is no longer met
            left += 1
        right += 1
    return min_window if min_length != float('inf') else ""

# Test the function
print(min_window_with_all_chars("adobecode", "abc"))  # Output: "adobec"

# ----------------------------------------------------------------------------------
# 5. Average of Sliding Window

"""
Average of Sliding Window
Task: Compute the average of all subarrays of size k.
Example: [1, 2, 3, 4], k=2 → [1.5, 2.5, 3.5]
Why: Directly supports Maximum Average Subarray I.
"""

def sliding_window_average(arr, k):
    """
    Computes the average of all subarrays of size k.
    
    - Uses a sliding window to compute sums, then averages them.
    - Time Complexity: O(n), Space Complexity: O(n) for result.
    - Simple and beginner-friendly with clear steps.
    """
    if len(arr) < k:
        return []
    window_sum = sum(arr[:k])
    averages = [window_sum / k]  # First window average
    for i in range(k, len(arr)):
        window_sum = window_sum - arr[i - k] + arr[i]
        averages.append(window_sum / k)
    return averages

# Test the function
print(sliding_window_average([1, 2, 3, 4], 2))  # Output: [1.5, 2.5, 3.5]