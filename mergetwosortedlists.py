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