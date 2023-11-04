'''138. Copy List with Random Pointer
Medium

A linked list of length n is given such that each node contains an additional random pointer,
 which could point to any node in the list, or null.

Construct a deep copy of the list.
 The deep copy should consist of exactly n brand new nodes,
  where each new node has its value set to the value of its corresponding original node.
   Both the next and random pointer of the new nodes should point to new nodes in the copied list
    such that the pointers in the original list and copied list represent the same list state.
     None of the pointers in the new list should point to nodes in the original list.

For example, if there are two nodes X and Y in the original list, where X.random --> Y,
 then for the corresponding two nodes x and y in the copied list, x.random --> y.

Return the head of the copied linked list.

The linked list is represented in the input/output as a list of n nodes.
Each node is represented as a pair of [val, random_index] where:

    val: an integer representing Node.val
    random_index: the index of the node (range from 0 to n-1)
     that the random pointer points to, or null if it does not point to any node.

Your code will only be given the head of the original linked list.

Example 1:

Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]

Example 2:

Input: head = [[1,1],[2,1]]
Output: [[1,1],[2,1]]

Example 3:

Input: head = [[3,null],[3,0],[3,null]]
Output: [[3,null],[3,0],[3,null]]



Constraints:

    0 <= n <= 1000
    -104 <= Node.val <= 104
    Node.random is null or is pointing to some node in the linked list.

'''
class Node:
    def __init__(self,val,next=None,random=None):
        self.val=val
        self.next=next
        self.random=random
def CopyRandomList(head):
    old_to_copy={None:None} #edge case what if next or random value is not connected so use like this None:None
    #if None comes means give value as None
    curr=head
    #Here there are 2 passes(2 loop) 1st one for copying values to our hashmap old_to_copy
    #2nd one for linking nodes and copy random pointers
    while curr:
        copy=Node(curr.val)
        old_to_copy[curr]=copy
        curr=curr.next #iterating to end

    curr = head  # Set the current node to the head of the original linked list
    while curr:
        copy = old_to_copy[curr]  # Access the copied node corresponding to the current original node
        copy.next = old_to_copy[curr.next]  # Set the 'next' pointer of the copied node to the next copied node
        copy.random = old_to_copy[curr.random]  # Set the 'random' pointer of the copied node to the copied random node
        curr = curr.next  # Move to the next node in the original linked list


def PrintCopy(head):
    result = []  # Initialize an empty list to store the nodes and their random pointers
    index = 0  # Initialize an index counter
    mapping = {}  # Initialize a dictionary to map nodes to their indices
    curr = head  # Set the current node to the head of the linked list

    # Loop to create a list representation of the nodes and their random pointers
    while curr:
        result.append([curr.val, None])  # Append [value, None] for each node to the result list
        mapping[curr] = index  # Map the current node to its index
        index += 1  # Increment the index counter
        curr = curr.next  # Move to the next node in the linked list

    index = 0  # Reset the index counter to 0
    curr = head  # Reset the current node to the head of the linked list

    # Loop to set the random pointers in the result list based on the mapping
    while curr:
        if curr.random:
            result[index][1] = mapping[curr.random]  # Set the random pointer to its index
        curr = curr.next  # Move to the next node
        index += 1  # Increment the index counter

    print(result)  # Print the resulting list representation of the linked list and its random pointers


# Create the linked list based on the input provided
#ie Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
#Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]
nodes = [Node(7), Node(13), Node(11),Node(10), Node(1)]
nodes[0].next = nodes[1]
nodes[1].next = nodes[2]
nodes[2].next = nodes[3]
nodes[3].next = nodes[4]

nodes[0].random = None
nodes[1].random = nodes[0]
nodes[2].random = nodes[4]
nodes[3].random = nodes[2]
nodes[4].random = nodes[0]


a=CopyRandomList(nodes[0])
PrintCopy(a)


