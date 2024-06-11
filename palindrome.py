


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=list("".join(c for c in s if c.isalpha()).lower())
        l,r = 0, len(s)-1
        print(s)
        print(s[l], l)
        print(s[r], r)
        
        while l<r:
            if(s[l] == s[r]):
                print(s[l])
                print(s[r])
                l += 1
                r -= 1
                continue
            else:
                return False
        return True
 
solution_instance = Solution()
input_string = "0P"
result = solution_instance.isPalindrome(input_string)
print(f'Is the string "{input_string}" a palindrome? {result}')