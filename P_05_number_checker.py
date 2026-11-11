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
            print(error)

# === Main Routine Goes Here ===
print("=== Area and Perimeter Calculator ===")

# 1. Get input from user using your num_check
width = num_check("Enter the width: ")
height = num_check("Enter the height: ")

# 2. Calculate Area and Perimeter
area = width * height
perimeter = 2 * (width + height)

# 3. Print Results (Exactly matching your PPT template!)
print()
print(f"Area: {area}")
print(f"Perimeter: {perimeter}")
