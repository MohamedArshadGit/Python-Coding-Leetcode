'''205. Isomorphic Strings
Solved
Easy
Topics
Companies

Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.


Example 1:

Input: s = "egg", t = "add"
Output: true

Example 2:

Input: s = "foo", t = "bar"
Output: false

Example 3:

Input: s = "paper", t = "title"
Output: true



Constraints:

    1 <= s.length <= 5 * 104
    t.length == s.length
    s and t consist of any valid ascii character.

Seen this question in a real interview before?
1/4
Yes
No
Accepted
1.1M
Submissions
2.5M
Acceptance Rate
43.4%
Topics
Hash Table
String'''
def isIsomorphic(s,t):
    mapST={} #creating two dictionaries for s to t mapping and t to s mapping
    mapTS={}
    for c1,c2 in zip(s,t): #iterating both at same time if we dont need we use two loops also
        if (c1 in mapST and mapST[c1]!=c2)or (c2 in mapTS and mapTS[c2]!=c1):# important ,to avoid
            #error bcos initally dictionary will be empty ,so we will 1st check if c1 in mapst and if st mapped value and c2 value is not same it means different charcter and return false same for mapTS also
            print(mapST)
            print(mapTS)
            return False
        mapST[c1]=c2 #mapping each letter of s to t
        mapTS[c2]=c1 #mapping each letter of t to s
    print(mapST)
    print(mapTS)
    return True

s = "egg"
t = "add"
a=isIsomorphic(s,t)
print(a)

s="foo"
t = "bar"
a=isIsomorphic(s,t)
print(a)

s = "paper"
t = "title"
a=isIsomorphic(s,t)
print(a)