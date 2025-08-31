import itertools

def truthTable(expression, variableList, expressionName):
    # Generate all combinations of True/False
    combos = list(itertools.product([False, True], repeat=len(variableList)))
    
    # Print header with the chosen expression name
    print("\t".join(variableList) + f"\t{expressionName}")
    print("-" * (8 * (len(variableList) + 1)))

    for combo in combos:
        env = dict(zip(variableList, combo))  # Assign values to variables
        result = eval(expression, {}, env)    # Evaluate the expression
        values = ["T" if val else "F" for val in combo]
        print("\t".join(values) + "\t" + ("T" if result else "F"))

# Ask user for variables
variableInput = input("Enter variables separated by spaces (e.g. A B C): ")
variableList = variableInput.split()

# Menu of expressions
print("\nChoose an expression:")
print("1. A and B")
print("2. A or B")
print("3. not A")
print("4. (A and B) or not C")

choice = input("Enter choice (1-4): ")

# Set expression and name based on choice
if choice == "1":
    expression = "A and B"
    expressionName = "A AND B"
elif choice == "2":
    expression = "A or B"
    expressionName = "A OR B"
elif choice == "3":
    expression = "not A"
    expressionName = "NOT A"
elif choice == "4":
    expression = "(A and B) or not C"
    expressionName = "(A AND B) OR NOT C"
else:
    print("Invalid choice!")
    exit()

# Generate truth table
truthTable(expression, variableList, expressionName)
