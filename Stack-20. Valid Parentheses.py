'''20. Valid Parentheses

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
 determine if the input string is valid.

An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.

Example 1:

Input: s = "()"
Output: true

Example 2:

Input: s = "()[]{}"
Output: true

Example 3:

Input: s = "(]"
Output: false

Constraints:

    1 <= s.length <= 104
    s consists of parentheses only '()[]{}'.

'''
def isValid(s):
    stack=[]
    close_to_open={")":"(","]":"[","}":"{"}
    for c in s:
        if c in close_to_open:
            if stack and stack[-1]==close_to_open[c]: #if stack means it is not empty and stack[-1] is last added value is equal to c
                stack.pop() #remove if matches ,our goal is to return empty stack that means everything is matching
            else:
                return False
        else:
            stack.append(c)
    #return True if len(stack)==0 else False
    return True if not stack else False

s = "()[]{}"
a=isValid(s)
print(a)

s = "(]"
a=isValid(s)
print(a)