
'''

a = [2,1,0]

def check(a):
    n = len(a)
    count = 0
    for i in range(n):
        if a[i] > a[(i + 1) % n]:
            count += 1
    return count <= 1

print(check(a)) 

'''

class Solution:
    def check(self, nums: List[int]) -> bool: # type: ignore
        n = len(nums)
        count = 0
        for i in range(n):
            if nums[i] > nums[(i + 1) % n]:
                count += 1
        return count <= 1