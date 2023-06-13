# O(nlogn) time | O(1) space - where n is the number of coins
def nonConstructibleChange(coins):
    # Write your code here.
    coins.sort()
    
    currentChange = 0
    for coin in coins:
        if coin > currentChange + 1:
            return currentChange + 1

        currentChange += coin
    
    return currentChange + 1
