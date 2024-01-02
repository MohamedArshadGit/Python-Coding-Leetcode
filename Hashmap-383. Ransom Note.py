'''383. Ransom Note
Solved
Easy
Topics
Companies

Given two strings ransomNote and magazine, return true if ransomNote can be constructed by
 using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false

Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false

Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true

Constraints:

    1 <= ransomNote.length, magazine.length <= 105
    ransomNote and magazine consist of lowercase English letters.

'''

def canConstruct(ransomnote,magazine):
    ransomnote_dict={} #initialize dictionary for both ransom and magazine to store how many each unquie characters are there
    magazine_dict={}
    for r_char in ransomnote:
        if r_char not in ransomnote_dict: #initially storing ransom note in ransomnote dict
            ransomnote_dict[r_char]=1
        else:
            ransomnote_dict[r_char]=ransomnote_dict[r_char]+1#if there are repeated same character we will increment to 1 eg: {'a':2}
    #print(ransomnote_dict)
    for m_char in magazine:
        if m_char not in magazine_dict: #same for magazine like ransom
            magazine_dict[m_char]=1
        else:
            magazine_dict[m_char]=magazine_dict[m_char]+1
    #print(magazine_dict)
    for char in ransomnote: #check if all ransomnote characters are in magazine_dict same as ransomnote chars or greater no of chars than ransom
        if char not in magazine_dict or magazine_dict[char]<ransomnote_dict[char]:
            #print(ransomnote_dict[char])
            return False
    return True

ransomNote = "aa"
magazine = "aab"
a=canConstruct(ransomNote,magazine)
print(a)

ransomNote = "a"
magazine = "b"
a=canConstruct(ransomNote,magazine)
print(a)

ransomNote = "aa"
magazine = "ab"
a=canConstruct(ransomNote,magazine)
print(a)