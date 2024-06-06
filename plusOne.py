class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        sum = int("".join(str(digit) for digit in digits)) +1
        print(sum)

        return [int(x) for x in str(sum)]
            
if __name__ == '__main__':
    a = Solution()
    a.plusOne([1,2,3,4])