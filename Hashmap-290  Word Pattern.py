'''290. Word Pattern

Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match,
such that there is a bijection between a letter in pattern and a non-empty word in s.

Example 1:

Input: pattern = "abba", s = "dog cat cat dog"
Output: true

Example 2:

Input: pattern = "abba", s = "dog cat cat fish"
Output: false

Example 3:

Input: pattern = "aaaa", s = "dog cat cat dog"
Output: false

Constraints:

    1 <= pattern.length <= 300
    pattern contains only lower-case English letters.
    1 <= s.length <= 3000
    s contains only lowercase English letters and spaces ' '.
    s does not contain any leading or trailing spaces.
    All the words in s are separated by a single space.

'''

def wordPattern(pattern,s):
    words=s.split(" ") #to make s as single words and ignore space we use split eg 'dog cat dog'=>"'dog','cat','dog'"
    if len(pattern)!=len(words):#if both length are not equal its not possible to do this program so return false incase
        return False
    pat_to_word={} #creating two dictionary for mapping letter to word and word to letter
    word_to_pat={}
    for c,w in zip(pattern,words):
        if (c in pat_to_word and pat_to_word[c]!=w) or (w in word_to_pat and word_to_pat[w]!=c):
            # important ,to avoid error bcos initally dictionary will be empty ,
            # so we will 1st check if c in pat_to_word and if pat_to_word mapped value and w value is not same it means different charcter and return false same for word_to_pat also
            return False
        pat_to_word[c]=w #mapping each letter of pattern to s
        word_to_pat[w]=c #mapping each word of s to pattern
    return True

pattern = "abba"
s = "dog cat cat dog"
a=wordPattern(pattern,s)
print(a)

pattern = "abba"
s = "dog cat cat fish"
a=wordPattern(pattern,s)
print(a)

pattern = "aaaa"
s = "dog cat cat dog"
a=wordPattern(pattern,s)
print(a)

