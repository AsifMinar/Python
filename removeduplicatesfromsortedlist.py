class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head):
        if not head or not head.next:
            return head
        
        current = head
        
        while current.next:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next
        
        return head
    

# Create a linked list: 1 -> 1 -> 2 -> 3 -> 3
node4 = ListNode(3)
node3 = ListNode(3, node4)
node2 = ListNode(2, node3)
node1 = ListNode(1, node2)
head = ListNode(1, node1)

# Create an instance of the Solution class
solution = Solution()

# Call the deleteDuplicates method passing the head of the linked list
result = solution.deleteDuplicates(head)

# Traverse the modified linked list and print the values
current = result
while current:
    print(current.val)
    current = current.next



