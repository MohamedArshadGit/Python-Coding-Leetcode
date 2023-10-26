'''150. Evaluate Reverse Polish Notation
Medium

You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

Evaluate the expression. Return an integer that represents the value of the expression.

Note that:

    The valid operators are '+', '-', '*', and '/'.
    Each operand may be an integer or another expression.
    The division between two integers always truncates toward zero.
    There will not be any division by zero.
    The input represents a valid arithmetic expression in a reverse polish notation.
    The answer and all the intermediate calculations can be represented in a 32-bit integer.

Example 1:

Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9

Example 2:

Input: tokens = ["4","13","5","/","+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6

Example 3:

Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
Output: 22
Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22
Constraints:

    1 <= tokens.length <= 104
    tokens[i] is either an operator: "+", "-", "*", or "/", or an integer in the range [-200, 200].

'''
def evalRPN(tokens):
    stack=[]
    for i in tokens:
        if i=="+":
            stack.append(stack.pop()+stack.pop())
        elif i=="-":
            a,b=stack.pop(),stack.pop() #- and / is different why we will pop last value and minus it will change the
            # order example[4,13,5,/,+] 1st 5 will be popped and 13 will be popped then 5/13 will come instead of 1
            # 13/5 so to avoid this initialise 2 varaible a and b and reverse it and minus it or divide it
            stack.append(b-a)
        elif i == "*":
            stack.append(stack.pop()*stack.pop()) # * and + has no issues because whatever we multiply from
            # reverse or vice versa answer is eg 2*3=6 and 3*2=6 so no issues
        elif i == "/":
            a, b = stack.pop(), stack.pop()
            stack.append(int(b/a))
        else:
            stack.append(int(i))
    return stack[0]

tokens = ["4","13","5","/","+"]
a=evalRPN(tokens)
print(a)

tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
a=evalRPN(tokens)
print(a)

tokens = ["2","1","+","3","*"]
a=evalRPN(tokens)
print(a)