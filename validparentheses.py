class Solution:
    def isValid(self, s):
        stack = []  # Create an empty stack to store opening brackets
        
        opening_brackets = ['(', '{', '[']  # List of opening brackets
        closing_brackets = [')', '}', ']']  # List of corresponding closing brackets
        
        bracket_pairs = {'(': ')', '{': '}', '[': ']'}  # Dictionary defining bracket pairs
        
        for char in s:  # Iterate through each character in the input string
            if char in opening_brackets:  # If the character is an opening bracket
                stack.append(char)  # Push it onto the stack
            elif char in closing_brackets:  # If the character is a closing bracket
                if not stack or bracket_pairs[stack.pop()] != char:
                    # If the stack is empty or the top element of the stack does not match the current closing bracket
                    return False  # Return False, as the parentheses are not valid
        
        return not stack  # Return True if the stack is empty (all opening brackets have been matched and popped), otherwise return False

# Example usage and input tests
solution = Solution()

# Example 1: Valid parentheses
input1 = "()"
print(solution.isValid(input1))  # Output: True

# Example 2: Valid parentheses
input2 = "()[]{}"
print(solution.isValid(input2))  # Output: True

# Example 3: Invalid parentheses
input3 = "(]"
print(solution.isValid(input3))  # Output: False

# Example 4: Invalid parentheses
input4 = "([)]"
print(solution.isValid(input4))  # Output: False

# Example 5: Valid parentheses
input5 = "{[]}"
print(solution.isValid(input5))  # Output: True