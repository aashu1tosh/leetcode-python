# Longest Substring without repeating characters

class Solution:
    def lengthOfLongestSubstring(self, s: str):
        l = 0
        my_set = set()
        res = 0
        for r in range(len(s)):
            while s[r] in my_set:
                my_set.remove(s[l])
                l += 1
            my_set.add(s[r])
            res = max(res, r-l+1)
        
        return res

if __name__ == '__main__':
    a = Solution()
    test_case = ["abcabcbb", "bbbbb", "pwwkew"]
    for test in test_case:
        print(f"passing {test}")
        ans = a.lengthOfLongestSubstring(test)
        print(f"The result for {test} is {ans}")
        print("-"*25)
    