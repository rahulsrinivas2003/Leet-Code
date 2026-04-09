class Solution(object):
    def mergeAlternately(self, word1, word2):
        
        merged = [] 

        for a,b in zip(word1, word2):

            merged.append(a+b)
        
        merged.append(word1[len(word2):])
        merged.append(word2[len(word1):])


        return "".join(merged)
        