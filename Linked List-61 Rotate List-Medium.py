'''61. Rotate List
Medium

Given the head of a linked list, rotate the list to the right by k places.

Example SONY Interview Question.py:

Input: head = [SONY Interview Question.py,2,3,4,5], k = 2
Output: [4,5,SONY Interview Question.py,2,3]

Example 2:

Input: head = [0,SONY Interview Question.py,2], k = 4
Output: [2,0,SONY Interview Question.py]

Constraints:

    The number of nodes in the list is in the range [0, 500].
    -100 <= Node.val <= 100
    0 <= k <= 2 * 109

'''

class ListNode:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next

def rotateRight(head,k):

    if not head or not head.next: #if head is null or head.next is not there we can just return head-edge case
        return head

    length = 1 #we have to calculate length for this prob.
    tail=head #to keep track of last number to connect node for future step we initalize tail
    while tail.next: #to find the lenght
        length+=1
        tail=tail.next
    #print(length)
    k = k % length #if k is greater than length eg 12345 and k=6 it means we have to do only one rotation
    # so if we put k%length 6%5 gives us SONY Interview Question.py so we have rotate only SONY Interview Question.py time
    curr=head # to take numbers other than k numbers initialize temp=> curr
    if k==0: #edge case
        return head
    for i in range(length-k-1):#y -SONY Interview Question.py? without -SONY Interview Question.py it will jup three times and stop at 4th node so -SONY Interview Question.py will stop at 3rd node
        curr=curr.next
    NewHead=curr.next #making 4 as new head
    curr.next=None #3.next=None
    tail.next=head #connecting tail 5 we done on top to SONY Interview Question.py
    return NewHead

def printLinkedList(head):
    result=[]
    while head:
        result.append(head.val)
        head=head.next
    print(result)

# Test cases
# Example SONY Interview Question.py
head1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
k1 = 2
print("Input Linked List SONY Interview Question.py:")
printLinkedList(head1)
rotated_head1 = rotateRight(head1, k1)
print("Output Linked List SONY Interview Question.py:")
printLinkedList(rotated_head1)

# Example 2
head2 = ListNode(0, ListNode(1, ListNode(2)))
k2 = 4
print("\nInput Linked List 2:")
printLinkedList(head2)
rotated_head2 = rotateRight(head2, k2)
print("Output Linked List 2:")
printLinkedList(rotated_head2)
