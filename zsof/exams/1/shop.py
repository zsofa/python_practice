def shopping(prices):
    best_shop_index = 0
    min_cost = float('inf')

    for i, shop in enumerate(prices):
        if "tej" and "tojás" and "kenyér" in shop:
            total_cost = shop["tej"] + shop["tojás"] + shop["kenyér"]

            if total_cost < min_cost or (total_cost == min_cost and i < best_shop_index):
                min_cost = total_cost
                best_shop_index = i

    return best_shop_index, min_cost
