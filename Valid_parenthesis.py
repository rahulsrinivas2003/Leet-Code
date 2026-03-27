class Solution(object):
    def isValid(self, s):    
        stack = []
        open_bracket = ["(", "{", "["]
        close_bracket = [")", "}", "]"]

        for i in range(len(s)):
            if s[i] in open_bracket:
                stack.append(s[i])
            else:
                if not stack:
                    return False
                top = stack.pop()
                if open_bracket.index(top) != close_bracket.index(s[i]):
                    return False
        
        return len(stack) == 0

                    


            

        