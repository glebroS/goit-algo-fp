import random


def simulate_dice_rolls(num_trials):
    results = {sum_val: 0 for sum_val in range(2, 13)}

    for _ in range(num_trials):
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        total = die1 + die2
        results[total] += 1

    return results


def calculate_probabilities(results, num_trials):
    probabilities = {sum_val: count / num_trials * 100 for sum_val, count in results.items()}
    return probabilities


if __name__ == "__main__":
    num_trials = 1000000
    results = simulate_dice_rolls(num_trials)
    probabilities = calculate_probabilities(results, num_trials)

    analytical_probs = {
        2: 2.78, 3: 5.56, 4: 8.33, 5: 11.11, 6: 13.89,
        7: 16.67, 8: 13.89, 9: 11.11, 10: 8.33, 11: 5.56, 12: 2.78
    }

    import sys
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except AttributeError:
        pass

    print(f"Результати симуляції Монте-Карло ({num_trials} кидків):")
    print(f"{'Сума':<6} | {'Кількість':<10} | {'Ймовірність (%)':<15} | {'Аналітична (%)':<15} | {'Відхилення (%)':<15}")
    print("-" * 75)

    for sum_val in range(2, 13):
        prob = probabilities[sum_val]
        analytical = analytical_probs[sum_val]
        deviation = abs(prob - analytical)
        print(f"{sum_val:<6} | {results[sum_val]:<10} | {prob:<15.2f} | {analytical:<15.2f} | {deviation:<15.2f}")
