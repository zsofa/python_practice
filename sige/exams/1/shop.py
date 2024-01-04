import sys

def shopping(prices):
    min_index = 0
    min_sum = sys.maxsize
    for i, element in enumerate(prices):
        sum_of_prices = element['tej'] + element['kenyér'] + element['tojás']
        if min_sum > sum_of_prices or (min_sum == sum_of_prices and i < min_index):
            min_sum = sum_of_prices
            min_index = i
    return min_index, min_sum
