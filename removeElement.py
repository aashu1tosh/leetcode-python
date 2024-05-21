nums = [3,2,2,3]
val =2
copynums = nums[:]
for num in nums:
    if num == val:
        copynums.remove(num)
nums = copynums[:]
print(nums)