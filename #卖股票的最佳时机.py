# 卖股票的最佳时机
# 因为股票是一天一天的过，不可能第二天买了用第一天的价钱卖出去，所以一次遍历即可
def maxProfit() -> int:
    prices = [7,1,5,3,6,4]
    max_pro = 0
    min_pri = prices[0]
    for i in prices:
        if i < min_pri:
            min_pri = i
        elif i - min_pri > max_pro:
            max_pro = i - min_pri
    print(max_pro)
    return max_pro
maxProfit()