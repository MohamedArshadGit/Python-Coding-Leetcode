'''2. Add Two Numbers

You are given two non-empty linked lists representing two non-negative integers.
 The digits are stored in reverse order, and each of their nodes contains a single digit.
 Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1:

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]

Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]

Constraints:

    The number of nodes in each linked list is in the range [1, 100].
    0 <= Node.val <= 9
    It is guaranteed that the list represents a number that does not have leading zeros.

'''
class ListNode: #to create linked list node -convention for singly linked list
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next

    def addTwoNumbers(self,l1,l2):
        l1= self.CreateLinkedList(l1)
        l2=self.CreateLinkedList(l2)

        dummy=ListNode()
        curr=dummy
        carry=0

        while l1 or l2 or carry: # carry edge case is very important why we need to check carry because at the end example if 7+8=15 5 will be added and 1 will be left
            # so at last iteration if carry is not 0 it will enter loop and add it in answer v1=0 v2=0 carry=1 finally 5 will be added
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            val=v1+v2+carry
            carry=val//10
            val=val%10
            new_node=ListNode(val)
            curr.next=new_node # Connect the 'curr' node to the newly created 'new_node', effectively adding it to the linked list.
            curr=curr.next #  preparing it for the next iteration.

            l1=l1.next if l1 else None
            l2 = l2.next if l2 else None
            #The lines l1 = l1.next if l1 else None and l2 = l2.next if l2 else None
            # are used to move to the next nodes in l1 and l2, respectively,
            # during the process of adding two linked lists.
            # These lines serve two important purposes:
            # Traversal: They allow you to traverse through the linked lists l1 and l2, node by node.
            # This is essential for adding the digits in the linked lists one by one,
            # just like how you would add numbers manually from right to left.

        return dummy.next


    def CreateLinkedList(self,arr):
        dummy=ListNode()  # Create a dummy node to serve as the starting point of the linked list
        curr=dummy # Initialize a variable 'curr' to point to the dummy node
        for i in arr:
            new_node=ListNode(i) #or we can write as current.next=ListNode(i) both are correct
            curr.next=new_node #we are linking new node to next node (convention in linked list it seems i was not sure)
            curr=curr.next #to iterate to next number we use this(similarly convention in linked list to iterate)
        return dummy.next # Return the actual head of the linked list (not the dummy node)

    def print_answer(self,head):
        curr=head
        result=[]
        while curr:
            result.append(curr.val)
            curr=curr.next
        print(result)

l1 = [2, 4, 3]
l2 = [5, 6, 4]
ll=ListNode()
ans=ll.addTwoNumbers(l1,l2)
ll.print_answer(ans)

l1 = [0]
l2 = [0]
ans=ll.addTwoNumbers(l1,l2)
ll.print_answer(ans)

l1 = [9, 9, 9, 9, 9, 9, 9]
l2 = [9, 9, 9, 9]
ans=ll.addTwoNumbers(l1,l2)
ll.print_answer(ans)
