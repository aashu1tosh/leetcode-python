class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i,j]
        
        hashmap = {}

        for i in range(len(nums)):
            print(nums[i])
            if target - nums[i] in hashmap:
                return [hashmap.get(target - nums[i]), i]
            else:
                hashmap.update({nums[i]: i})
            
            print(hashmap)
        

        

        
solution_instance = Solution()
nums = [2,7,11,15]
target = 9
result = solution_instance.twoSum(nums, target)
print(f'{result} are the index that sum to target')