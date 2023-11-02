'''21. Merge Two Sorted Lists

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list.
The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Example 1:

Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:

Input: list1 = [], list2 = []
Output: []

Example 3:

Input: list1 = [], list2 = [0]
Output: [0]

Constraints:

    The number of nodes in both lists is in the range [0, 50].
    -100 <= Node.val <= 100
    Both list1 and list2 are sorted in non-decreasing order.
'''

class ListNode:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next
    def mergeTwoLists(self,list1,list2):
        list1=  self.createLinkedList(list1)#to run in pycharm we need to create Linked list in leetcode inbuilt code will be there
        list2 = self.createLinkedList(list2)

        dummy=ListNode() #logic starts from here
        curr=dummy

        while list1 and list2: #we should iterate till list is empty
            if list1.val<list2.val: #which is lesser add it 1st so if and else
                curr.next=list1
                list1=list1.next
            else:
                curr.next=list2
                list2=list2.next
            curr=curr.next #we can put in if condition block and else block 2 times but this is shortcut

        if list1:
            curr.next=list1 #edge case if there are extra number in any other list like 1 list has 123 another list has 1234
        if list2:
            curr.next=list2

        return dummy.next

    def createLinkedList(self,arr): #taken from add two numbers linked list problem
        dummy=ListNode()
        curr=dummy
        for i in arr:
            curr.next=ListNode(i)
            curr=curr.next
        return dummy.next

    def print_ans(self,value):
        result=[]
        curr=value
        while curr:
            result.append(curr.val)
            curr=curr.next
        print(result)

list1 = [1,2,4]
list2 = [1,3,4]

ll=ListNode()
value=ll.mergeTwoLists(list1,list2)
ll.print_ans(value)