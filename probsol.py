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




class solution:
    def lcp(self, strs):
        if not strs:
            return ""
        
        sorted_strs = sorted(strs)
        fs = sorted_strs[0]
        ls = sorted_strs[-1]

        prefix = ""
        for i in range(len(fs)):
            if fs[i] == ls[i]:
                prefix += fs[i]
            else:
                break
        return prefix
    
solution = solution()
print(solution.lcp(["flower","flow","flight"]))



class Solution:
    def isValid(self, s):
        stack = []  # Create an empty stack to store opening brackets
        
        opening_brackets = ['(', '{', '[']  # List of opening brackets
        closing_brackets = [')', '}', ']']  # List of corresponding closing brackets
        
        bracket_pairs = {'(': ')', '{': '}', '[': ']'}  # Dictionary defining bracket pairs
        
        
        for char in s:  # Iterate through each character in the input string
            if char in opening_brackets:  # If the character is an opening bracket
                stack.append(char)  # Push it onto the stack
                #print(bracket_pairs[stack.pop()])
            elif char in closing_brackets:  # If the character is a closing bracket
                #print(bracket_pairs[stack.pop()])
                if not stack or bracket_pairs[stack.pop()] != char:
                    #print(bracket_pairs[stack.pop()])
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

# Example 5: Valid parentheses
input6 = "]"
print(solution.isValid(input6))  # Output: False





# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1, l2):
        # Create a dummy node to serve as the head of the merged list
        dummy = ListNode(0)
        current = dummy
        
        # Traverse both lists simultaneously
        while l1 and l2:
            # Compare the values of the current nodes of l1 and l2
            if l1.val <= l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next
        
        # Append the remaining elements of the non-empty list
        current.next = l1 or l2
        
        # Return the merged list (excluding the dummy head)
        return dummy.next  
    
# Example usage
# Create the first linked list: 1 -> 2 -> 4
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(4)
node2.next = node3
node1.next = node2
l1 = node1

# Create the second linked list: 1 -> 3 -> 4
node4 = ListNode(1)
node5 = ListNode(3)
node6 = ListNode(4)
node5.next = node6
node4.next = node5
l2 = node4

# Create an instance of the Solution class
solution = Solution()

# Merge the two lists
merged_list = solution.mergeTwoLists(l1, l2)

# Print the values of the merged list
current = merged_list
while current:
    print(current.val, "->", end=" ")
    current = current.next
print("None")




class Solution:
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        
        unique = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[unique - 1]:
                nums[unique] = nums[i]
                unique += 1

        return unique


# Example usage
nums = [1, 1, 2, 2, 3, 3, 4, 5, 5]
solution = Solution()
length = solution.removeDuplicates(nums)

print("Original Array:", nums)
print("Length:", length)
print("Modified Array:", nums[:length])





def removeElement(nums, val):
        count = 0
        
        for i in range(len(nums)):
            if nums[i] != val:
                nums[count] = nums[i]
                count += 1
        
        return count


nums = [3, 2, 2, 3, 4, 5, 3, 4, 5]
val = 3

length = removeElement(nums, val)

print("Original Array:", nums)
print("Length:", length)
print("Modified Array:", nums[:length])  





class Solution:
    def strStr(self, haystack, needle):
        if needle == "":
            return 0
        if needle not in haystack:
            return -1
        return haystack.index(needle)

# Example usage
haystack = "sadbutsad"
needle = "sad"

solution = Solution()
index = solution.strStr(haystack, needle)

print("Haystack:", haystack)
print("Needle:", needle)
print("Index of the First Occurrence:", index)






class Solution:
    def searchInsert(self, nums, target):
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return left

# Example usage
nums = [1, 3, 5, 6]
target = 5

solution = Solution()
position = solution.searchInsert(nums, target)

print("Target:", target)
print("Position:", position)







class Solution:
    def lengthOfLastWord(self, nums):
        
        for i in range (len(nums)):
          if nums[i] == " ":
            n = 0
          else:
            n += 1
            f = n 

        return f 

# Example usage
nums = "  full moon  "


solution = Solution()
position = solution.lengthOfLastWord(nums)

print("Position:", position)





class Solution:
    def plusOne(self, nums):
        sum = ""
        for i in nums:
          sum = sum + str(i)
          
        sum = int(sum) + 1

        nl = [int(d) for d in str(sum)]

        return nl

# Example usage
nums = [1,0]


solution = Solution()
position = solution.plusOne(nums)


print("Position:", position)







class Solution:
    def addBinary(self, a, b):
        carry = 0
        result = ""
        
        i, j = len(a) - 1, len(b) - 1
        
        while i >= 0 or j >= 0 or carry > 0:
            digit_a = int(a[i]) if i >= 0 else 0
            digit_b = int(b[j]) if j >= 0 else 0
            
            current_sum = digit_a + digit_b + carry
            
            carry = current_sum // 2
            digit = current_sum % 2
            
            result = str(digit) + result
            
            i -= 1
            j -= 1
        
        return result


# Example usage
a = "11"
b = "1"

solution = Solution()
result = solution.addBinary(a, b)

print("Result:", result)






class Solution:
    def mySqrt(self, x):
        if x == 0:
            return 0
        
        left, right = 1, x
        
        while left <= right:
            mid = left + (right - left) // 2
            sqrt = x // mid  # Using integer division
            
            if sqrt == mid:
                return mid
            elif sqrt < mid:
                right = mid - 1
            else:
                left = mid + 1
        
        # If the exact square root is not found, return the floor value
        return right


# Example usage
x = 16

solution = Solution()
result = solution.mySqrt(x)

print("Square root of", x, "is:", result)







class Solution:
    def climbStairs(self, n):
        if n <= 2:
            return n
        
        prev_1 = 1
        prev_2 = 2
        
        for _ in range(3, n + 1):
            current = prev_1 + prev_2
            prev_1 = prev_2
            prev_2 = current
        
        return prev_2


# Example usage
n = 3

solution = Solution()
result = solution.climbStairs(n)

print("Number of distinct ways to climb to the top:", result)


'''








class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head):
        if not head or not head.next:
            return head
        
        current = head
        
        while current.next:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next
        
        return head
    

# Create a linked list: 1 -> 1 -> 2 -> 3 -> 3
node4 = ListNode(3)
node3 = ListNode(3, node4)
node2 = ListNode(2, node3)
node1 = ListNode(1, node2)
head = ListNode(1, node1)

# Create an instance of the Solution class
solution = Solution()

# Call the deleteDuplicates method passing the head of the linked list
result = solution.deleteDuplicates(head)

# Traverse the modified linked list and print the values
current = result
while current:
    print(current.val)
    current = current.next


















