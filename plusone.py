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