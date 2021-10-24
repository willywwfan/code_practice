def stockPairs(stocksProfit, target):
    pair_list = []
    for i in range(target-1):
        pair_list.append((i+1,target-i-1))

    if target%2 == 1:
        pair_list = pair_list[:int((target-1)/2)]
    else:
        pair_list = pair_list[:int((target)/2)]
    # print(pair_list)

    pair_num = 0
    for pair in pair_list:
        if pair[0] in stocksProfit and pair[1] in stocksProfit:
            pair_num += 1
    return pair_num

if __name__ == '__main__':


    stocksProfit = [6,12,3,9,3,5,1,12]


    target = 7

    result = stockPairs(stocksProfit, target)

    print(result)
