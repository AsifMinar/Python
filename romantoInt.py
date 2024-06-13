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
print(solution.romanToInt("LVIII"))  # Expected output: 58
print(solution.romanToInt("MCMXCIV"))  # Expected output: 1994