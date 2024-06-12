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