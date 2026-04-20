class Solution:
    def reverseWords(self, s: str) -> str:
        
        stripped_string = s.strip()

        arr = stripped_string.split()

        arr.reverse()

        return " ".join(arr)

         
