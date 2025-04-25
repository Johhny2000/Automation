from itertools import combinations_with_replacement

# Get best possible deal for cash-cards
def find_min_cost_cash_cards(target_value):
    options = [
        #{"value": 150, "cost": 139.99},
        #{"value": 100, "cost": 93.99},
        #{"value": 80, "cost": 77.99},
        #{"value": 75, "cost": 69.49},
        #{"value": 60, "cost": 59.99},
        {"value": 50, "cost": 43.99},
        #{"value": 30, "cost": 29.49},
        {"value": 20, "cost": 17.99},
        #{"value": 10, "cost": 11.99},
        #{"value": 5, "cost": 5.99}
    ]

    best_cost = float('inf')
    best_combination = []

    # Check all possible combinations of cash-cards
    for i in range(1, target_value // 20 + 2):  # Maximum number of cards needed
        for combination in combinations_with_replacement(options, i):
            total_value = sum(card['value'] for card in combination)
            total_cost = sum(card['cost'] for card in combination)

            # Only consider combinations that meet or exceed the target value
            if total_value >= target_value and total_cost < best_cost:
                best_cost = total_cost
                best_combination = combination

    return best_combination, best_cost


# Get user input
try:
    target_value = float(input("Enter the amount of cash-cards required (in EUR): "))
    total_card_value = 0
    if target_value <= 0:
        print("Please enter a positive amount.")
    else:
        selected_cards, total_cost = find_min_cost_cash_cards(int(target_value))

        print("\nSelected cash-cards:")
        for card in selected_cards:
            print(f"  - {card['value']} EUR card, Cost: {card['cost']} EUR")
            total_card_value += card['value']

        print(f"\nTotal card value: {total_card_value} EUR")
        print(f"Total cost: {total_cost:.2f} EUR")
        print(f"Total savings: {(total_card_value-total_cost):.2f} EUR")


except ValueError:
    print("Invalid input. Please enter a numeric value.")
