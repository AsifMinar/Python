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

'''

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





