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
    print("\n=== Ultimate Unit Converter ===")
    print("1. Time (Seconds to Hours)")
    print("2. Distance (mm to meters)")
    print("3. Mass (g to kg)")

    choice = input("Choose a conversion (1-3): ").strip()

    if choice == "1":
        print("\n--- Time Converter (Seconds -> Hours) ---")
        seconds = num_check("Enter time in seconds: ")
        hours = seconds / 3600
        print(f"{seconds} seconds is equal to {hours:.4f} hours")

    elif choice == "2":
        print("\n--- Distance Converter (mm -> m) ---")
        mm = num_check("Enter distance in mm: ")
        meters = mm / 1000
        print(f"{mm} mm is equal to {meters:.3f} meters")

    elif choice == "3":
        print("\n--- Mass Converter (g -> kg) ---")
        grams = num_check("Enter mass in grams: ")
        kg = grams / 1000
        print(f"{grams} g is equal to {kg:.3f} kg")

    else:
        print("Invalid choice! Please select between 1 and 3.")

    print()
    keep_going = input("Do you want to do another conversion? (yes/no): ").strip()

print("\nThank you for using the Ultimate Converter. Goodbye!")
