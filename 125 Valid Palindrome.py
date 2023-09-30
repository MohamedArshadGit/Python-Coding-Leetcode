'''125. Valid Palindrome

A phrase is a palindrome if,
 after converting all uppercase letters into lowercase letters
  and removing all non-alphanumeric characters, it reads the same forward and backward.
  Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.

Constraints:
    1 <= s.length <= 2 * 105
    s consists only of printable ASCII characters.

'''

#EASY WAY AND USING INBUILTFUNCTIONS
def isPalindrome(s):
    rev=""
    s=s.lower()
    for i in s:
        if i.isalnum():
            rev=rev+i
    return rev==rev[::-1]

s = "A man, a plan, a canal: Panama"
a=isPalindrome(s)
print(a)

#WITHOUT USING INBUILT FUNCTION-TOUGH METHOD -USEFUL FOR INTERVUEW
class Solution(object):
    def ISPALINDROME(self,s):
        left=0
        right=len(s)-1
        s=s.lower()
        while left<right:
            while left<right and not self.ALPHANUMERIC(s[left]):
                left+=1
            while right>left and not self.ALPHANUMERIC(s[right]):
                right-=1
            if s[left]!=s[right]:
                return False
            left=left+1
            right=right-1
        return True

    def ALPHANUMERIC(self,c):
        return (ord('A')<=ord(c)<=ord('Z')or
                ord('a')<=ord(c)<=ord('z')or
                ord('0')<=ord(c)<=ord('9'))
    '''def ALPHANUMERIC(self,c):
            return (ord('a')<=ord(c)<=ord('z') or ord('0')<=ord(c)<=ord('9'))'''
    '''def ALPHANUMERIC(self, c):
        # Check if the character is alphanumeric (letters or digits)
        return ('a' <= c <= 'z' or '0' <= c <= '9')'''

solution=Solution()
s = "race a car"
sa = "A man, a plan, a canal: Panama"
result=solution.ISPALINDROME(sa)
print(result)