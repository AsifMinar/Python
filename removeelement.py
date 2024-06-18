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


'''
 def removeElement(self, nums, val):
        count = 0
        
        for num in nums:
            if num != val:
                nums[count] = num
                count += 1
        
        return count
        
'''