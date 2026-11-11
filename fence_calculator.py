def num_check(question):
    error = "Please enter a number that is more than zero\n"
    while True:
        try:
            response = float(input(question))
            if response > 0:
                return response
            else:
                print(error)
        except ValueError:
            print("Please enter a number.")


# === Main Routine Goes Here ===
keep_going = "yes"
while keep_going.lower() == "yes" or keep_going.lower() == "y":
    print("\n=== Fence Cost Calculator ===")

    # 1. Get user inputs using num_check
    width = num_check("Enter the width of the area (m): ")
    length = num_check("Enter the length of the area (m): ")
    cost_per_meter = num_check("Enter the cost of fencing per meter ($): ")

    # 2. Calculate Perimeter and Total Cost
    perimeter = 2 * (width + length)
    total_cost = perimeter * cost_per_meter

    # 3. Print results
    print("\n--- Results ---")
    print("Perimeter: " + str(perimeter) + " meters")
    print("Total Cost of Fencing: $" + str(total_cost))
    print("---------------")

    # 4. Ask to loop again (Requirement: possible to do more than one calculation)
    print()
    keep_going = input("Do you want to calculate another fence? (yes/no): ").strip()

print("\nThank you for using the Fence Calculator. Goodbye!")
