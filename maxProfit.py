prices = [1,2,4,2,5,7,2,4,9,0,9]
# prices = [3,2,6,5,0,3]

l,r =0,1
maxProfit = 0
while r<len(prices):
    if prices[r]-prices[l] <= 0:
        l += 1
        r += 1
    if prices[r] < prices[l]:
        l=r
        r +=1
    if prices[r]-prices[l] >=0:
        if maxProfit < prices[r]-prices[l]:
            maxProfit = prices[r]-prices[l]
        r +=1
print(maxProfit)