def cumulative_product(lst):
    cumul_prod = [1]
    for i in range(1, len(lst)):
        cumul_prod.append(cumul_prod[-1] * lst[i])
    return cumul_prod
lst = [1, 2, 3, 4]
cumul_prod = cumulative_product(lst)
print("Cumulative product:", cumul_prod)
