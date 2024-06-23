class Solution:
    def climbStairs(self, n: int) -> int:
        result = [1,1]

        for i in range(n-1):
            num = result[0] + result[1]
            result.insert(0,num)
            print(result)
        
        return result[0]

soultion = Solution()
soultion.climbStairs(3)