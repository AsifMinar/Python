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