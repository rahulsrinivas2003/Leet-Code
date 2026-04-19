class Solution:
    def reverseVowels(self, s: str) -> str:
        
        vowels = "aeiouAEIOU"
        arr = list(s)
        first_pointer , last_pointer = 0, len(arr) - 1

        while first_pointer <= last_pointer:

            while first_pointer < last_pointer and arr[first_pointer] not in vowels:

                first_pointer += 1
            while first_pointer < last_pointer and arr[last_pointer] not in vowels:

                last_pointer -= 1
            arr[first_pointer] , arr[last_pointer] = arr[last_pointer] , arr[first_pointer]
            first_pointer +=1 
            last_pointer -=1 
        
        return "".join(arr)
        