# It is a sweltering summer day, and a boy wants to buy some ice cream bars.

# At the store, there are n ice cream bars. You are given an array costs of length n, where costs[i] is the price of the ith ice cream bar in coins. The boy initially has coins coins to spend, and he wants to buy as many ice cream bars as possible. 

# Return the maximum number of ice cream bars the boy can buy with coins coins.

# Note: The boy can buy the ice cream bars in any order.

 

# Example 1:

# Input: costs = [1,3,2,4,1], coins = 7
# Output: 4
# Explanation: The boy can buy ice cream bars at indices 0,1,2,4 for a total price of 1 + 3 + 2 + 1 = 7.
# Example 2:

# Input: costs = [10,6,8,7,7,8], coins = 5
# Output: 0
# Explanation: The boy cannot afford any of the ice cream bars.
# Example 3:

# Input: costs = [1,6,3,1,2,5], coins = 20
# Output: 6
# Explanation: The boy can buy all the ice cream bars for a total price of 1 + 6 + 3 + 1 + 2 + 5 = 18.
 

# Constraints:

# costs.length == n
# 1 <= n <= 105
# 1 <= costs[i] <= 105
# 1 <= coins <= 108








class Solution(object):
    def maxIceCream(self, costs, coins):
        icecream=0

        for i in sorted(costs):
            if coins-i>=0:
                coins=coins-i
                icecream=icecream+1
  
        return icecream




n=Solution
arr=[27,23,33,26,46,86,70,85,89,82,57,66,42,18,18,5,46,56,42,82,52,78,4,27,96,74,74,52,2,24,78,18,42,10,12,10,80,30,60,38,32,7,98,26,18,62,50,42,15,14,32,86,93,98,47,46,58,42,74,69,51,53,58,40,66,46,65,2,10,82,94,26,6,78,2,101,97,16,12,18,71,5,46,22,58,12,18,62,61,51,2,18,34,12,36,58,20,12,17,70]
print(n.maxIceCream(n,arr,241))