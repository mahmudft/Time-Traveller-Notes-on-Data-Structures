"""
Check if two strings are valid anagram

F.E

"anagram", "nagaram"   => True

"car"  "cat"

"""

from collections import Counter

def validAnagramm(x: str, y: str):

    if len(x) != len(y):
        return False
            
    return Counter(x) == Counter(y)

print(validAnagramm("anagram", "nagaram"))