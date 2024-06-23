class Solution:
    def isValid(self, s: str) -> bool:
        mylist = [i for i in s]
        stack = []

        for bracket in mylist:    
            if bracket in '({[':
                stack.append(bracket)
            else:
                if not stack or \
                    ( bracket == ')' and stack[-1] != '(' ) or \
                    ( bracket == '}' and stack[-1] != '{' ) or \
                    ( bracket == ']' and stack[-1] != '[' ):
                        print(False)
                        break
                stack.pop()
            
        return not stack

solution = Solution()
print(solution.isValid('([{}]'))
