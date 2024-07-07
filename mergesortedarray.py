class Solution:
    def merge(self, nums1, m, nums2, n):
        while n > 0:
            if m <= 0 or nums2[n - 1] >= nums1[m - 1]:
                nums1[m + n - 1] = nums2[n - 1]
                n -= 1
            else:
                nums1[m + n - 1] = nums1[m - 1]
                m -= 1


# Example input
nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3

# Create an instance of the Solution class
solution = Solution()

# Call the merge method with the given input
solution.merge(nums1, m, nums2, n)

# Print the merged array
print(nums1)