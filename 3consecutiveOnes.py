class Solution:
    def threeConsecutiveOdds(self, arr: list[int]) -> bool:
        for i in range(len(arr)-2):
            if arr[i] % 2 == 1 and arr[i+1] % 2 == 1 and arr[i+2] % 2 == 1:
                return True
        return False

if __name__ == '__main__':
    a = Solution()
    print(a.threeConsecutiveOdds([1,2,34,3,4,5,7,23,12]))