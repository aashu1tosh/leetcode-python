# nums = [2,2,1,1,1,2,2]
nums = [3,3,4]

count = {}
result, maxCount = 0,0

#MY CODE
# for i,num in enumerate(nums):
#     count[num] = 1 + count.get(num, 0)
#     if maxCount < count[num]:
#         res = num
#         maxCount = count[num]

#A bit better code
for num in nums:
    count[num] = 1 + count.get(num, 0)
    res = num if(maxCount < count[num]) else res
    maxCount = max(count[num], maxCount)

print(maxCount, "max Count")
print(res, "number repeated max times")
print(count, "the hash map")
