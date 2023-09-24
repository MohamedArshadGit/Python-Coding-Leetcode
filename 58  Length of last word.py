'''58. Length of Last Word

Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal
substring
consisting of non-space characters only.

Example 1:

Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.

Example 2:

Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.

Example 3:

Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.
'''
# My own Method
def lengthoflastword(s):
    s=s.strip()
    word_length=0
    #print(s)
    #print(len(s)-1)
    for i in range(len(s)-1,-1,-1):
        if s[i] != ' ':
            word_length += 1
        print(s[i])
        if s[i] == ' ':
            break
    return word_length


s = "   fly me   to   the moon  "
result=lengthoflastword(s)
print(result)

print()
#Method without using Inbuilt function
def lenoflastword(a):
    i=len(a)-1
    word_length=0
    while a[i]==' ':
        i=i-1
    while i>=0 and a[i]!=' ':
        word_length+=1
        print(a[i])
        i=i-1
    return word_length

a = "luffy is still joyboy"
res=lenoflastword(a)
print(res)



