#HW4 part 2

value_dict = {
    'cito': 47.999,
    'BB_studio': 42.999,
    'momo': 49.999,
    'main-service': 37.245,
    'buy_now': 38.324,
    'x-store': 37.166,
    'the_partner': 38.988,
    'sota': 37.720,
    'rozetka': 38.003,
}

lower_limit = float(input('Введите нижний порог -> '))
upper_limt = float(input('Введите верхний порог -> '))

results_dict = {}

for brand, price in value_dict.items():
    if lower_limit < price < upper_limt:
        results_dict[brand] = price

print(results_dict)



