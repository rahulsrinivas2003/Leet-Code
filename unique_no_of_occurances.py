from collections import Counter
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        
        repeat = []
        arr = Counter(arr)

        for occurance in arr.values():

            if occurance not in repeat:

                repeat.append(occurance)
            else:

                return False
        
        return True



        