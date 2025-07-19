# CM to Inch Converter
def cm_to_inch():
    try:
        cm = float(input("Centimeter(s): "))
        inches = cm / 2.54
        print("Inch(es):", inches)
    except ValueError:
        print("Error: Please enter a valid number")

# Inch to CM Converter
def inch_to_cm():
    try:
        inches = float(input("Inch(es): "))
        cm = inches * 2.54
        print("Centimeter(s):", cm)
    except ValueError:
        print("Error: Please enter a valid number")

# Kilogram to LBS Converter
def kg_to_lbs():
    try:
        kg = float(input("Kilogram(s): "))
        lbs = kg * 2.204623
        print("LBS:", lbs)
    except ValueError:
        print("Error: Please enter a valid number")

# LBS to Kilogram Converter
def lbs_to_kg():
    try:
        lbs = float(input("LBS: "))
        kg = lbs / 2.204623
        print("Kilogram(s):", kg)
    except ValueError:
        print("Error: Please enter a valid number")

# Meter to Foot Converter
def meter_to_foot():
    try:
        meter = float(input("Meter(s): "))
        foot = meter * 3.2808399
        print("Feet:", foot)
    except ValueError:
        print("Error: Please enter a valid number")

while True:
    print("\n--- MetricsCalc ---")
    print("1. CM to Inches")
    print("2. Inches to CM")
    print("3. KG to LBS")
    print("4. LBS to KG")
    print("5. Meter to Foot")
    print("6. Exit")
    
    try:
        choice = input("Enter your choice (1-6): ").strip()
        
        if choice == '1':
            cm_to_inch()
        elif choice == '2':
            inch_to_cm()
        elif choice == '3':
            kg_to_lbs()
        elif choice == '4':
            lbs_to_kg()
        elif choice == '5':
            meter_to_foot()
        elif choice == '6':
            print("Thanks for using MetricsCalc!")
            break
        else:
            print("Invalid choice. Please select a number between 1-6")
    except ValueError:
        print("Invalid choice. Please select a number between 1-6")