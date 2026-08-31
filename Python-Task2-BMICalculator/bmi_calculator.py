def get_positive_float(prompt):
    """Validates inputs to ensure they are positive numeric values."""
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("❌ Error: Value must be greater than zero.")
                continue
            return value
        except ValueError:
            print("❌ Error: Invalid input. Please enter a valid number.")


def classify_bmi(bmi):
    """Classifies the BMI into standard health categories."""
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25.0:
        return "Normal"
    elif 25.0 <= bmi < 30.0:
        return "Overweight"
    else:
        return "Obese"


def main():
    print("=" * 40)
    print("        OIB SIP - BMI CALCULATOR        ")
    print("=" * 40)

    # 1. Prompt user for weight (kg) and height (m) with input validation
    weight = get_positive_float("Enter your weight in kilograms (kg): ")
    height = get_positive_float("Enter your height in meters (m): ")

    # 2. Calculate BMI using formula
    bmi = weight / (height**2)

    # 3. Classify result into categories
    category = classify_bmi(bmi)

    # 4. Display the BMI value rounded to 2 decimal places and the category
    print("-" * 40)
    print(f"📊 Your calculated BMI is: {bmi:.2f}")
    print(f"📌 Health Category: {category}")
    print("=" * 40)


if __name__ == "__main__":
    main()

