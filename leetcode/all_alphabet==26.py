# A pangram is a sentence where every letter of the English alphabet appears at least once.

# Given a string sentence containing only lowercase English letters, return true if sentence is a pangram, or false otherwise.

 

# Example 1:

# Input: sentence = "thequickbrownfoxjumpsoverthelazydog"
# Output: true
# Explanation: sentence contains at least one of every letter of the English alphabet.
# Example 2:

# Input: sentence = "leetcode"
# Output: false
 

# Constraints:

# 1 <= sentence.length <= 1000
# sentence consists of lowercase English letters.



class Solution(object):
    def checkIfPangram(self, sentence):
        return len(set(sentence)) == 26



n=Solution
print(n.checkIfPangram(n,"abcdefghijklmnopqrstuvwxyzcdsjxhghfdgwdsxfatda"))
print(n.checkIfPangram(n,"fghijklmnopqrstuvwxyzcdsjxhghfdgwdsxfatda"))


