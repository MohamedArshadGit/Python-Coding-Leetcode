'''242. Valid Anagram
Solved
Easy
Topics
Companies

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.



Example 1:

Input: s = "anagram", t = "nagaram"
Output: true

Example 2:

Input: s = "rat", t = "car"
Output: false



Constraints:

    1 <= s.length, t.length <= 5 * 104
    s and t consist of lowercase English letters.



Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?
Seen this question in a real interview before?
1/4
Yes
No
Accepted
3M
Submissions
4.7M
Acceptance Rate
64.0%
Topics
Hash Table
String
Sorting'''

#Neet Method
def isAnagram(s,t):
    if len(s)!=len(t): #anagram is possible only with equal length so we put if loop
        return False
    hash_s={} #creating two hash table(dictionary) for storing  frequency of each character
    # from string s and t
    hash_t={}
    for i in range(len(s)):#we are iterating through length of s
        hash_s[s[i]]=1+hash_s.get(s[i],0) #hash_s.get(s[i], 0): This checks if the character s[i] is already a key in hash_s. If it is, it returns the value associated with it. If not, it returns 0 (a default value).
        hash_t[t[i]]=1+hash_t.get(t[i],0) #1 + hash_s.get(s[i], 0): This takes the value obtained from the previous step (either the count of s[i] or 0) and adds 1 to it.

        #or simple method we can use like this given below
        '''if s[i] not in hash_s:
            hash_s[s[i]]=SONY Interview Question.py
        else:
            hash_s[s[i]]+=SONY Interview Question.py
        if t[i] not in hash_t:
            hash_t[t[i]]=SONY Interview Question.py
        else:
            hash_t[t[i]]+=SONY Interview Question.py'''
    #print("Hash-s:",hash_s)
    #print("Hash-t:", hash_t)
    for char in hash_s:
        if hash_s[char]!=hash_t.get(char,0): #we are comparing whether frequency of each characters are same,if not it is not a anagram so return false
            #we use get for hash_t bcos we are iterating through hash_s if hash_s char is not present in hash_t will throw error so we use get for hash_t
            #print(hash_s[char])
            #print(hash_t.get(char,0))
            return False

    return True

s = "anagram"
t = "nagaram"
a=isAnagram(s,t)
print(a)
s = "rat"
t = "car"
a=isAnagram(s,t)
print(a)
print()

'''My own Method using 383 RANSOM NOTE SUM'''
def isAnagram(s, t):
    s_dict={}
    t_dict={}

    if len(s)!=len(t):
        return False

    for c in s:
        if c not in s_dict:
            s_dict[c]=1 #adding count of each char
        else:
            s_dict[c]+=1 #if already char is there incrementing the number
    for c1 in t:
        if c1 not in t_dict:
            t_dict[c1]=1
        else:
            t_dict[c1]+=1
    '''what .get() do if word in s_dict not present in t_dict it will throw key error so t_dict.get(char,0) will give count if that char is present if that char eg c is not present in t_dict it will give 0 as default '''
    for char in s_dict: #In next line we use get for hash_t bcos we are iterating through hash_s if hash_s char is not present in hash_t will throw error so we use get for hash_t
        if s_dict[char]!=t_dict.get(char,0): #Iteration 3: char = 't's_dict['t'] is 1t_dict.get('t', 0) is 0 (because 't' doesn't exist in t_dict, defaulting to 0)Since s_dict['t'] is not equal to t_dict.get('t', 0) (1 != 0), the condition is satisfied.
            print("s_dict:", s_dict)
            print("t_dict", t_dict)
            return False
    print("s_dict:", s_dict)
    print("t_dict",t_dict)
    return True

s = "anagram"
t = "nagaram"
a=isAnagram(s,t)
print(a)
s = "rat"
t = "car"

a=isAnagram(s,t)
print(a)
print()

#another easiest way with inbuilt functions- in one line of code
'''from collections import Counter #import counter
def IsAnagram(s,t):
    return Counter(s)==Counter(t) #it will count for strings automatically if equal will return true
    #return sorted(s)==sorted(t) #this is another method sort all the letters with inbuilt function of equal it returns true
s = "rat"
t = "car"
a=IsAnagram(s,t)
print(a)

s = "anagram"
t = "nagaram"
a=IsAnagram(s,t)
print(a)
print()'''