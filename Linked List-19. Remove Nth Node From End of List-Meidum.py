'''19. Remove Nth Node From End of List
Medium

Given the head of a linked list, remove the nth node from the end of the list and return its head.

Example 1:

Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:

Input: head = [1], n = 1
Output: []

Example 3:

Input: head = [1,2], n = 1
Output: [1]

Constraints:

    The number of nodes in the list is sz.
    1 <= sz <= 30
    0 <= Node.val <= 100
    1 <= n <= sz

Follow up: Could you do this in one pass?
'''

class ListNode:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next
def removeNthFromEnd(head,n):
    dummy=ListNode(0,head)
    left=dummy
    right=dummy.next #or right=head
    while n>0 and right:#means right not equal to null,
        # why this loop because we need to shift right pointer to n times
        right=right.next
        n-=1
    while right:
        left=left.next
        right=right.next

    left.next=left.next.next # this line says eg if [3,4,5] next of 3 is equal to 3.next.next which is == 5
    #ie from 3 4 5 to  3=>5
    return dummy.next
# Function to print the linked list
def printLinkedList(head):
    result = []
    while head:
        result.append(head.val)
        head=head.next
    print(result)


# Test cases
# Example 1
head1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
n1 = 2
print("Input Linked List 1:")
printLinkedList(head1)
modified_head1 = removeNthFromEnd(head1, n1)
print("Output Linked List 1:")
printLinkedList(modified_head1)

# Example 2
head2 = ListNode(1)
n2 = 1
print("\nInput Linked List 2:")
printLinkedList(head2)
modified_head2 = removeNthFromEnd(head2, n2)
print("Output Linked List 2:")
printLinkedList(modified_head2)

# Example 3
head3 = ListNode(1, ListNode(2))
n3 = 1
print("\nInput Linked List 3:")
printLinkedList(head3)
modified_head3 = removeNthFromEnd(head3, n3)
print("Output Linked List 3:")
printLinkedList(modified_head3)
