#Best time to sell and buy stocks problem

#Brute force approach 
#Time: O(N*N), Space: O(1)
def maxProfitBForce(prices):
    profit = 0
    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            if prices[j] - prices[i] > profit:
                profit = prices[j] - prices[i]
    return profit

#Two pointer approch
#Time: O(N), Space: O(1)
def maxProfitTPointer(prices):
    profit = 0
    l, r = 0, 1
	#While l < len(prices):
    for _ in range(len(prices)-1):
        if prices[r] > prices[l]:
            curProfit = prices[r] - prices[l]
            profit = max(profit, curProfit)
        else:
            l  = r
        r += 1
    return profit

#Dynamic Programming
#Time: O(N), Space: O(1)
def maxProfitDProgramming(prices):
    buy = prices[0]
    profit = 0
    for i in range(1, len(prices)):
        if prices[i] < buy:
            buy = prices[i]
        elif prices[i] - buy > profit:
            profit = prices[i] - buy
    return profit

# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Input: prices = [7,6,4,3,1]
# Output: 0