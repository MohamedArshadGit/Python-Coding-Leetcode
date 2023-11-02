'''92. Reverse Linked List II-Medium

Medium

Given the head of a singly linked list and two integers left and right where left <= right,
 reverse the nodes of the list from position left to position right, and return the reversed list.


Example 1:

Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]

Example 2:

Input: head = [5], left = 1, right = 1
Output: [5]

Constraints:

    The number of nodes in the list is n.
    1 <= n <= 500
    -500 <= Node.val <= 500
    1 <= left <= right <= n
'''
class ListNode:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next

    def Reverse_linked_list(self,head,left,right):
        dummy = ListNode(0, head)
        leftprev = dummy
        curr = head
        for i in range(left - 1):
            leftprev = curr
            curr = curr.next

        nextpoint = None
        for i in range((right - left) + 1):
            tempnext = curr.next # stores the reference to the next node that needs to be processed before changing the curr pointer to it.
            curr.next = nextpoint # this is masterstroke line veryvery imp. it makes 2 node points to nullThis line changes the curr.next pointer to point to the previous node (nextpoint).
            # Essentially, it reverses the direction of the pointer.
            nextpoint = curr #nextpoint = curr: nextpoint is then moved to the current node curr, updating it as the new head of the reversed sublist.curr = tempnext: curr is moved forward to the next node in the original order to continue the reversal process.
            curr = tempnext

        leftprev.next.next = curr #leftprev need to points to null like 1 2 null we are making 5.next as null chatgpt-This line connects the last node of the reversed sublist to the node immediately after the reversed sublist.
        leftprev.next = nextpoint #swapping 4 to 2 by using nextpoint which is stored
        return dummy.next

    def printLinkedList(self,head):
        result=[]
        while head:
            result.append(head.val)
            head=head.next

        print(result)



# Test cases
# Example 1
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
left = 2
right = 4
ll=ListNode()
a =ll.Reverse_linked_list(head, left, right)
print("Output Linked List 1:")
ll.printLinkedList(a)




head2 = ListNode(5)
left2 = 1
right2 = 1
a=ll.Reverse_linked_list(head2,left2,right2)
ll.printLinkedList(a)