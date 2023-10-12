# https://leetcode.com/problems/valid-anagram/

# A valid anagram is a word with exactly the same letters as other words. 
def isAnagram(self, s: str, t: str) -> bool:
        # If the lengths are not the same they can never be a valid anagram
        if len(s) != len(t):
            return False

        # Create 2 dictonaries to count each letter in the word
        countS, countT = {}, {}
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        
        # Check if the dictonaries are the same
        return countS == countT
