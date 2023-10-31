'''141. Linked List Cycle

Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list
 that can be reached again by continuously following the next pointer.
 Internally, pos is used to denote the index of the node that tail's next pointer is connected to.
  Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

Example 1:

Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

Example 2:

Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.

Example 3:

Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.

Constraints:

    The number of the nodes in the list is in the range [0, 104].
    -105 <= Node.val <= 105
    pos is -1 or a valid index in the linked-list.

Follow up: Can you solve it using O(1) (i.e. constant) memory?
'''
class ListNode: #initiate node for linked list
    def __init__(self,val=None,next=None):
        self.val=val
        self.next=next

    def hasCycle(self,head):
        slow=head # here we are using Floyd's Tortoise and Hare algo
        fast=head
        while fast and fast.next: #its should not be null if it is null it means there is no cycle
            slow=slow.next #move by 1 shift
            fast=fast.next.next #move by 2 shift
            if slow==fast:
                return True
        return False

    def createLinkedList(self,values,pos):
        nodes=[ListNode(val) for val in values] #to create nodes 1st we cant pass list directly in linked list
        # we need to create each node and link each node like given below

        for i in range(len(nodes)-1): #y -1 because we are leaving last nodes not connected to anything
            nodes[i].next=nodes[i+1] #linking the current node to next node

        if pos>=0 and pos<len(nodes):
            nodes[-1].next=nodes[pos] #to connect the pos node with last node we use like this nodes[-1].next
            # in this .next is given to create a loop to connect with given position

        return nodes[0]
'''
    def printLinkedList(self, head): #for my testing i did this
        current = head
        while current:
            print(current.val, end=" -> ")
            current = current.next

    def getLength(self, head):
        length = 0
        current = head
        while current:
            length += 1
            current = current.next
        return length'''

values=[3, 2, 0, -4]
pos=1
ll=ListNode()
a=ll.createLinkedList(values,pos)
print(ll.hasCycle(a))
#print(ll.printLinkedList(a))
#print(ll.getLength(a))

values=[1, 2]
pos=0
a=ll.createLinkedList(values,pos)
print(ll.hasCycle(a))

values=[1]
pos=-1
a=ll.createLinkedList(values,pos)
print(ll.hasCycle(a))



