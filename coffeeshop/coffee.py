def collect_ingredient_customization():
    """
    Collect ingredient customization details and return as a dictionary.
    """
    # Sugar
    while True:
        try:
            sugar = int(input("How many teaspoons of sugar? (0-5): ").strip())
            if 0 <= sugar <= 5:
                break
            else:
                print("Please enter a number between 0 and 5.")
        except ValueError:
            print("Please enter a valid number.")

    # Cream/Milk
    while True:
        try:
            cream = int(input("How much cream/milk? (0-100 ml, in 10ml increments): ").strip())
            if 0 <= cream <= 100 and cream % 10 == 0:
                break
            else:
                print("Please enter a multiple of 10 between 0 and 100.")
        except ValueError:
            print("Please enter a valid number.")

    # Additional flavors
    flavors_available = {
        "1": "Vanilla",
        "2": "Caramel",
        "3": "Hazelnut",
        "4": "Chocolate",
        "5": "None"
    }

    print("\nAvailable Flavors:")
    for key, flavor in flavors_available.items():
        print(f"{key}. {flavor}")

    while True:
        flavor_choice = input("Select a flavor (1-5): ").strip()
        if flavor_choice in flavors_available:
            selected_flavor = flavors_available[flavor_choice]
            break
        else:
            print("Invalid selection. Please choose a number between 1 and 5.")

    # Whipped cream topping
    whipped_cream = input("Add whipped cream? (yes/no): ").strip().lower()
    whipped_cream = whipped_cream in ["yes", "y"]

    # Cinnamon or cocoa powder
    # Cinnamon or cocoa powder: require a valid choice, but treat empty input as 'none'
    valid_powders = ["cinnamon", "cocoa", "none"]
    while True:
        powder = input("Add cinnamon or cocoa powder? (cinnamon/cocoa/none) [Enter for none]: ").strip().lower()
        if powder == "":
            powder = "none"
            break
        if powder in valid_powders:
            break
        print("Invalid selection. Please enter 'cinnamon', 'cocoa', or 'none' (or press Enter for none).")

    return {
        "sugar": sugar,
        "cream": cream,
        "flavor": selected_flavor,
        "whipped_cream": whipped_cream,
        "powder": powder
    }


def order_coffee():
    """
    Prompt user to order coffee and provide a confirmation.
    """
    print("Welcome to the Coffee Shop!")
    print("-" * 40)

    # Get user's name
    user_name = input("What is your name? ").strip()

    # Display available coffee options
    coffee_menu = {
        "1": "Espresso",
        "2": "Americano",
        "3": "Latte",
        "4": "Cappuccino",
        "5": "Mocha",
        "6": "Macchiato"
    }

    print("\nAvailable Coffees:")
    for key, coffee in coffee_menu.items():
        print(f"{key}. {coffee}")

    # Get coffee selection
    while True:
        choice = input("\nSelect your coffee (1-6): ").strip()
        if choice in coffee_menu:
            selected_coffee = coffee_menu[choice]
            break
        else:
            print("Invalid selection. Please choose a number between 1 and 6.")

    # Get quantity
    while True:
        try:
            quantity = int(input("How many cups would you like? ").strip())
            if quantity > 0:
                break
            else:
                print("Quantity must be greater than 0.")
        except ValueError:
            print("Please enter a valid number.")

    # Size selection will be requested after deciding customization scope
    sizes_map = {"S": "Small", "M": "Medium", "L": "Large"}

    # Get ingredient customization
    print("\n--- Ingredient Customization ---")

    # Check if customization per cup is needed for multiple cups
    customizations = []

    if quantity > 1:
        per_cup_customization = input(f"Do you need different customization for each of the {quantity} cups? (yes/no): ").strip().lower()
        per_cup_customization = per_cup_customization in ["yes", "y"]
    else:
        per_cup_customization = False

    if per_cup_customization:
        # Collect customization for each cup individually (ask size per cup if applicable)
        for cup_num in range(1, quantity + 1):
            print(f"\n--- Cup {cup_num} Customization ---")
            while True:
                size_choice = input(f"Select size for cup {cup_num} (S/M/L): ").strip().upper()
                if size_choice in sizes_map:
                    cup_size = sizes_map[size_choice]
                    break
                else:
                    print("Invalid size. Please choose S, M, or L.")

            cup_customization = collect_ingredient_customization()
            cup_customization["size"] = cup_size
            customizations.append(cup_customization)
    else:
        # Collect single customization for all cups (ask size once if applicable)
        if quantity > 1:
            print("(This customization will apply to all cups)")
        while True:
            size_choice = input("Select size (S/M/L): ").strip().upper()
            if size_choice in sizes_map:
                size = sizes_map[size_choice]
                break
            else:
                print("Invalid size. Please choose S, M, or L.")

        base_customization = collect_ingredient_customization()
        base_customization["size"] = size
        customizations = [base_customization] * quantity

    # Generate confirmation
    print("\n" + "=" * 40)
    print("ORDER CONFIRMATION")
    print("=" * 40)
    print(f"Customer Name: {user_name}")
    print(f"Coffee: {selected_coffee}")
    print(f"Size: {size}")
    print(f"Quantity: {quantity} cup(s)")
    print("\n--- Customization Details ---")

    for idx, customization in enumerate(customizations, 1):
        if len(customizations) > 1:
            print(f"\nCup {idx}:")
        # Print per-cup size if available
        if "size" in customization:
            print(f"  Size: {customization['size']}")
        else:
            print(f"  Size: {size}")
        print(f"  Sugar: {customization['sugar']} teaspoon(s)")
        print(f"  Cream/Milk: {customization['cream']} ml")
        print(f"  Flavor: {customization['flavor']}")
        print(f"  Whipped Cream: {'Yes' if customization['whipped_cream'] else 'No'}")
        print(f"  Topping: {customization['powder'].capitalize() if customization['powder'] != 'none' else 'None'}")

    print("=" * 40)
    print(f"Total: ${quantity * 4.50:.2f}")
    print("=" * 40)
    print("Thank you for your order! Your coffee will be ready shortly.\n")


if __name__ == "__main__":
    order_coffee()
