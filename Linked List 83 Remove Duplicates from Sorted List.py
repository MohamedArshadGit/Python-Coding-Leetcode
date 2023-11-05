'''82. Remove Duplicates from Sorted List II

Medium

Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.

Example 1:

Input: head = [1,2,3,3,4,4,5]
Output: [1,2,5]

Example 2:

Input: head = [1,1,1,2,3]
Output: [2,3]



Constraints:

    The number of nodes in the list is in the range [0, 300].
    -100 <= Node.val <= 100
    The list is guaranteed to be sorted in ascending order.

'''
class ListNode:
    def __init__(self,val=None,next=None):
        self.val=val
        self.next=next
def deleteDuplicates(head):
    curr=head
    while curr: #curr is not null
        while curr.next and curr.next.val==curr.val: #curr.next is not null and curr.next.val ==curr,val it means duplicates
            curr.next=curr.next.next #so shift to next 2 numbers(shift to unique)
        curr=curr.next #to iterate curr after running 2 loop iteration once

    return head #why we are not returning curr because curr will point at null curr will point at end so return head

def printLinkedList(head):
    result=[]
    while head:
        result.append(head.val)
        head=head.next
    print(result)

# Test cases
# Example 1
head1 = ListNode(1, ListNode(1, ListNode(2)))
print("Input Linked List 1:")
printLinkedList(head1)
modified_head1 = deleteDuplicates(head1)
print("Output Linked List 1:")
printLinkedList(modified_head1)

# Example 2
head2 = ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(3)))))
print("\nInput Linked List 2:")
printLinkedList(head2)
modified_head2 = deleteDuplicates(head2)
print("Output Linked List 2:")
printLinkedList(modified_head2)