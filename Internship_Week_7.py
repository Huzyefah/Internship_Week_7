# Constants
NUM_CHARITIES = 3

# Task 1 - Set up the donation system
def setup_donation_system():
    charities = []
    totals = [0] * NUM_CHARITIES

    # Input charity names
    for i in range(NUM_CHARITIES):
        charity_name = input(f"Enter the name of charity {i + 1}: ")
        charities.append(charity_name)

    # Display charity names with numbers
    for i, charity in enumerate(charities):
        print(f"{i + 1}. {charity}")

    return charities, totals


# Task 2 - Record and total each donation
def record_and_total_donation(charities, totals):
    while True:
        try:
            choice = int(input("Enter the number of the chosen charity (1, 2, 3), or -1 to show totals: "))

            if choice == -1:
                show_totals(charities, totals)
                break

            if choice not in [1, 2, 3]:
                print("Error: Invalid choice. Please enter 1, 2, 3, or -1.")
                continue

            bill_amount = float(input("Enter the value of the customer's shopping bill: "))

            donation = bill_amount * 0.01
            totals[choice - 1] += donation

            print(f"Donation of ${donation:.2f} recorded for {charities[choice - 1]}.")

        except ValueError:
            print("Error: Invalid input. Please enter a valid number.")

# Task 3 - Show the totals so far
def show_totals(charities, totals):
    total_donated = sum(totals)
    
    # Sort charities and totals in descending order of totals
    sorted_charities_totals = sorted(zip(charities, totals), key=lambda x: x[1], reverse=True)

    # Display charities and totals
    for charity, total in sorted_charities_totals:
        print(f"{charity}: ${total:.2f}")

    print(f"GRAND TOTAL DONATED TO CHARITY: ${total_donated:.2f}")


# Test the program
charities, totals = setup_donation_system()
record_and_total_donation(charities, totals)
