'''# fibonacci series

def fibonacci(n):
    a = 0
    b = 1
    if n==1:
        print(a)
    else:
        print(a)
        print(b)
        for i in range(2,n):
            c = a + b
            a = b
            b = c
            print(c)

fibonacci(10)


def twoSum(nums, target):
    # Get the length of the input list
    n = len(nums)
    
    # Iterate through each element in the list
    for i in range(n):
        
        # Iterate through the remaining elements
        # starting from the next index
        for j in range(i + 1, n):
            
            # Check if the sum of the current element
            # and any other element equals the target value
            if nums[i] + nums[j] == target:
                
                # If a pair is found, return their indices
                return [i, j]
    
    # If no pair is found, return an empty list
    return []

# Test the function with some sample inputs 
print(twoSum([2, 7, 11, 15], 9))  # Output: [0, 1]
print(twoSum([3, 2, 4], 6))       # Output: [1, 2]






def ts(nums, target):
    n = len(nums)
    for i in range(n):
        for j in range(i+1, n):
            if nums[i] + nums[j] == target:
                return [i,j]
    return []

print(ts([2,7,11,15],9))





# Define the Solution class
class Solution:
    def isPalindrome(self, x):
        # Check if the number is negative
        if x < 0:
            return False
        
        # Convert the integer to a string
        nums = str(x)
        
        # Iterate over the first half of the string up to the middle index
        for i in range(len(nums) // 2):
            # Compare the character at index i with its symmetric counterpart
            # at len(nums) - i - 1
            if nums[i] != nums[len(nums) - i - 1]:
                # If the characters are not equal, it's not a palindrome
                return False
        
        # If the loop completes without finding any unequal characters,
        # it is a palindrome
        return True

# Create an instance of the Solution class
solution = Solution()

# Test cases
print(solution.isPalindrome(121))  # Expected output: True
print(solution.isPalindrome(-121))  # Expected output: False
print(solution.isPalindrome(10))  # Expected output: False





class Solution:
    def romanToInt(self, s):
        # Create a dictionary to map Roman numerals to their respective integer values
        roman_to_int = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        # Initialize the result variable
        result = 0
        
        # Iterate through the Roman numeral string
        for i in range(len(s)):
            # Get the integer value of the current Roman numeral
            value = roman_to_int[s[i]]
            
            # If the current value is less than the next value, subtract it from the result
            if i < len(s) - 1 and value < roman_to_int[s[i + 1]]:
                result -= value
            # Otherwise, add it to the result
            else:
                result += value
        
        return result


# Create an instance of the Solution class
solution = Solution()

# Test cases
print(solution.romanToInt("III"))  # Expected output: 3
print(solution.romanToInt("IV"))  # Expected output: 4
print(solution.romanToInt("IX"))  # Expected output: 9
print(solution.romanToInt("LIVII"))  # Expected output: 56
print(solution.romanToInt("MCMXCIV"))  # Expected output: 1994


'''

class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""  # If the input list is empty, return an empty string as there are no strings to compare.
        
        # Sort the array of strings
        sorted_strs = sorted(strs)  # Sorting the list of strings helps find the common prefix efficiently.
        
        # Consider the first and last string in the sorted array
        first_str = sorted_strs[0]  # The first string in the sorted list.
        last_str = sorted_strs[-1]  # The last string in the sorted list.
        
        # Find the common prefix between the first and last string
        prefix = ""
        for i in range(len(first_str)):  # Iterate through the characters of the first string.
            if first_str[i] == last_str[i]:  # If the characters at the same index are equal,
                prefix += first_str[i]  # add the character to the prefix string.
            else:
                break  # If the characters are not equal, we have found the end of the common prefix.
        
        return prefix  # Return the common prefix string.
    

solution = Solution()

# Example 1:
strs = ["flower", "flow", "flight"]
# The common prefix among the strings "flower", "flow", and "flight" is "fl".
print(solution.longestCommonPrefix(strs))  # Output: "fl"

# Example 2:
strs = ["dog", "racecar", "car"]
# There is no common prefix among the strings "dog", "racecar", and "car".
print(solution.longestCommonPrefix(strs))  # Output: ""

# Example 3:
strs = ["apple", "ape", "apricot"]
# The common prefix among the strings "apple", "ape", and "apricot" is "ap".
print(solution.longestCommonPrefix(strs))  # Output: "ap"