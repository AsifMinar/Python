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