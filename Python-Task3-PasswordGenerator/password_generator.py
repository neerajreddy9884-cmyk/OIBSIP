import random
import string


def generate_password():
    print("\n" + "=" * 45)
    print("     OIB SIP - PASSWORD GENERATOR     ")
    print("=" * 45)

    # 1. Prompt and enforce minimum 8 characters length
    while True:
        try:
            length = int(input("Enter desired password length (minimum 8): "))
            if length < 8:
                print("❌ Error: Password length must be at least 8 characters.")
                continue
            break
        except ValueError:
            print("❌ Error: Please enter a valid whole number.")

    # 2. Prompt user to choose character types
    print("\nSelect character pools to include:")
    inc_lower = input("Include lowercase letters? (y/n): ").strip().lower() == "y"
    inc_upper = input("Include uppercase letters? (y/n): ").strip().lower() == "y"
    inc_digits = input("Include numeric digits? (y/n): ").strip().lower() == "y"
    inc_symbols = input("Include special symbols? (y/n): ").strip().lower() == "y"

    # Enforce at least 2 pools are selected
    selected_pools = sum([inc_lower, inc_upper, inc_digits, inc_symbols])
    if selected_pools < 2:
        print(
            "\n❌ Validation Error: You must select at least 2 character types for security."
        )
        return

    # Build character selection pools
    char_pool = ""
    mandatory_chars = []

    if inc_lower:
        char_pool += string.ascii_lowercase
        mandatory_chars.append(random.choice(string.ascii_lowercase))
    if inc_upper:
        char_pool += string.ascii_uppercase
        mandatory_chars.append(random.choice(string.ascii_uppercase))
    if inc_digits:
        char_pool += string.digits
        mandatory_chars.append(random.choice(string.digits))
    if inc_symbols:
        char_pool += string.punctuation
        mandatory_chars.append(random.choice(string.punctuation))

    # Fill remaining password length randomly from the combined pool
    remaining_length = length - len(mandatory_chars)
    remaining_chars = [random.choice(char_pool) for _ in range(remaining_length)]

    # Combine pools and shuffle to ensure random distribution
    password_list = mandatory_chars + remaining_chars
    random.shuffle(password_list)
    password = "".join(password_list)

    # 3. Display the final password
    print("-" * 45)
    print(f"🔒 Your Secure Password is: {password}")
    print("=" * 45)


def main():
    while True:
        generate_password()

        # Option to generate another password without restarting the program
        again = (
            input("\nWould you like to generate another password? (y/n): ")
            .strip()
            .lower()
        )
        if again != "y":
            print("Thank you for using the Password Generator. Goodbye!")
            break


if __name__ == "__main__":
    main()


