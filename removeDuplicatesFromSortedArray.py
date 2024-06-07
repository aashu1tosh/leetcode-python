# nums = [1, 1, 2]
nums = [0,0,1,1,1,2,2,3,3,4]
# copy = nums[:]

# for i in range(len(nums)):
#     if nums[i] == nums [i-1]:
#         copy.remove(nums[i])

# nums = copy[:]
# print(nums)


copy = nums[:]
for i in range(len(nums)-1):
    if nums[i] == nums [i+1]:
        copy.remove(nums[i])
nums = copy[:]

print(nums)