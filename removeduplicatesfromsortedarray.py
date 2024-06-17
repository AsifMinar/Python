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