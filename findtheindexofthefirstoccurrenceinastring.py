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

