# https://leetcode.com/problems/group-anagrams/
from collections import defaultdict

# This groups a list of anagrams together
# By counting the letters of each word 
# And using the array as key of the dictonary
def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        allAnagrams = defaultdict(list)
        for i in strs:
            allAnagrams[stringToArr(i)].append(i)
        return allAnagrams.values()

# This binds every letter from a to z in a array which is afterwards converted to a string
def stringToArr(t):
    result = [0] * 26
    for i in t:
        result[ord('z') - ord(i)] = result[ord('z') - ord(i)] + 1
    return str(result)
