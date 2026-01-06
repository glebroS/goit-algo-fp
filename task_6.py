def greedy_algorithm(items, budget):
    items_list = []
    for name, details in items.items():
        ratio = details['calories'] / details['cost']
        items_list.append({
            'name': name,
            'cost': details['cost'],
            'calories': details['calories'],
            'ratio': ratio
        })

    items_list.sort(key=lambda x: x['ratio'], reverse=True)

    selected_items = []
    total_cost = 0
    total_calories = 0

    for item in items_list:
        if total_cost + item['cost'] <= budget:
            selected_items.append(item['name'])
            total_cost += item['cost']
            total_calories += item['calories']

    return selected_items, total_calories, total_cost


def dynamic_programming(items, budget):
    item_names = list(items.keys())
    item_costs = [items[name]['cost'] for name in item_names]
    item_calories = [items[name]['calories'] for name in item_names]
    n = len(items)

    dp = [[0 for _ in range(budget + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(budget + 1):
            cost = item_costs[i-1]
            calories = item_calories[i-1]

            if cost <= w:
                dp[i][w] = max(dp[i-1][w], dp[i-1][w-cost] + calories)
            else:
                dp[i][w] = dp[i-1][w]

    selected_items = []
    w = budget
    total_calories = dp[n][budget]

    for i in range(n, 0, -1):
        if dp[i][w] != dp[i-1][w]:
            selected_items.append(item_names[i-1])
            w -= item_costs[i-1]

    return selected_items, total_calories


if __name__ == "__main__":
    items = {
        "pizza": {"cost": 50, "calories": 300},
        "hamburger": {"cost": 40, "calories": 250},
        "hot-dog": {"cost": 30, "calories": 200},
        "pepsi": {"cost": 10, "calories": 100},
        "cola": {"cost": 15, "calories": 220},
        "potato": {"cost": 25, "calories": 350}
    }

    budget = 100

    import sys
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except AttributeError:
        pass

    print(f"Бюджет: {budget}")

    greedy_selection, greedy_cal, greedy_cost = greedy_algorithm(items, budget)
    print("\nЖадібний алгоритм:")
    print(f"Вибрані страви: {greedy_selection}")
    print(f"Сумарна калорійність: {greedy_cal}")
    print(f"Сумарна вартість: {greedy_cost}")

    dp_selection, dp_cal = dynamic_programming(items, budget)
    dp_cost = sum(items[item]['cost'] for item in dp_selection)

    print("\nДинамічне програмування:")
    print(f"Вибрані страви: {dp_selection}")
    print(f"Сумарна калорійність: {dp_cal}")
    print(f"Сумарна вартість: {dp_cost}")
