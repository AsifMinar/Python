class Solution:
    def twoSum(self, nums, target):
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []

# Create an instance of the Solution class
solution = Solution()

# Take input from the user for the nums list
nums = input("Enter a list of numbers (space-separated): ").split()
nums = [int(num) for num in nums]

# Take input from the user for the target value
target = int(input("Enter the target value: "))

# Call the twoSum method on the instance
result = solution.twoSum(nums, target)

# Print the result
if result:
    print(f"The indices of the two numbers that add up to the target are: {result}")
else:
    print("No such pair found.")