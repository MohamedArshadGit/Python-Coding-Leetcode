'''227. Basic Calculator II
Medium
Given a string s which represents an expression, evaluate this expression and return its value.

The integer division should truncate toward zero.

You may assume that the given expression is always valid.
 All intermediate results will be in the range of [-231, 231 - 1].

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions,
such as eval().

Example 1:

Input: s = "3+2*2"
Output: 7

Example 2:

Input: s = " 3/2 "
Output: 1

Example 3:

Input: s = " 3+5 / 2 "
Output: 5

Constraints:

    1 <= s.length <= 3 * 105
    s consists of integers and operators ('+', '-', '*', '/') separated by some number of spaces.
    s represents a valid expression.
    All the integers in the expression are non-negative integers in the range [0, 231 - 1].
    The answer is guaranteed to fit in a 32-bit integer.

'''

def calculate(s):
    stack=[] #to store numbers other than / and *
    curr_num=0 #initialise
    operator="+"#in start itself y we initialise + is because to append number to stack we need some operator initially
    all_operators={"+","-","*","/"} #storing all operators if anyone comes we will use it
    nums=set(str(i) for i in range(10)) #it will store number from 0-9 it will be used to check whether a string is number or not
    for i in range(len(s)):
        data=s[i] #initialise data
        if data in nums:
            curr_num=curr_num*10+int(data) #this is called as truncation y used?
            # example if single digit like 3 or 4 or 5 cames means no issues
            # if 2 or 3 digit numbers came like 345 567 we need to use like this so we use this formula
        if data in all_operators or i==(len(s)-1): #y or because loop stops after appending  so to run till the end we use this edge case if u remove error will be thrown
            if operator=="+":
                stack.append(curr_num)
                print(stack)
            elif operator=="-":
                stack.append(-curr_num)
                print(stack)
            elif operator== "*":
                stack[-1]*=curr_num
            elif operator == "/":
                stack[-1]=int(stack[-1]/curr_num) #very big issue created by this one line
                # see the difference between int(3/2) and 3//2 in note refer note
            curr_num=0 #reset current num
            operator=data #change the operator value to current input value
    print(stack)
    return sum(stack) #finally adding all the numbers inside the stack and returning it

s="14-3/2"
a=calculate(s)
print(a)

s="10-4+3*2+10/5"
a=calculate(s)
print(a)

s = "3+2*2"
a=calculate(s)
print(a)

s = " 3/2 "
a=calculate(s)
print(a)

s = " 3+5 / 2 "
a=calculate(s)
print(a)