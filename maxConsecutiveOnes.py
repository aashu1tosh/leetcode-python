class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        m1 = 0
        count = 0
        for data in nums:
            if(data == 1):
                count +=1
            else:
                m1 = max(m1, count)
                count =0
        m1 = max(m1, count)
        return m1
    
if __name__ == '__main__':
    a = Solution()
    a.findMaxConsecutiveOnes([1,2,1,1,1,4])