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



'''

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



