import sys
from math import gcd

def count_coprime_pairs(a, b, c, d):
    count = 0
    for x in range(a, b + 1):
        for y in range(c, d + 1):
            if gcd(x, y) == 1:
                count += 1
    return count

def get_input(prompt):
    """ Safely gets integer input from the user with a formatted prompt. """
    while True:
        try:
            print("*" * 50)
            value = int(input(f"{prompt}"))
            print("*" * 50)
            if value < 1:
                print("Error: Please enter a positive integer.")
            else:
                return value
        except ValueError:
            print("Error: Invalid input. Please enter a valid integer.")

def main():
    while True:  # Main loop to keep the application running
        print("*" * 50)
        print("* Welcome to the Encryption Strength Calculator *")
        print("*" * 50)
        print("You will be asked to enter two intervals. Each interval")
        print("consists of a start and an end, both positive integers.")
        
        a = get_input("Enter the start of the first interval (a): ")
        b = get_input("Enter the end of the first interval (b) where b >= a: ")
        while b < a:
            print("Error: End of the interval must be greater than or equal to the start.")
            b = get_input("Re-enter the end of the first interval (b) where b >= a: ")

        c = get_input("Enter the start of the second interval (c): ")
        d = get_input("Enter the end of the second interval (d) where d >= c: ")
        while d < c:
            print("Error: End of the interval must be greater than or equal to the start.")
            d = get_input("Re-enter the end of the second interval (d) where d >= c: ")

        # Computing the strength of the encryption algorithm
        strength = count_coprime_pairs(a, b, c, d)
        print("*" * 50)
        print(f"* The strength of the encryption algorithm is: {strength} *")
        print("*" * 50)

        # Ask the user if they want to continue or exit
        continue_choice = input("Type 'exit' to stop or press Enter to calculate again: ")
        if continue_choice.lower() == 'exit':
            print("Exiting the Encryption Strength Calculator. Goodbye!")
            break  # Break the loop to exit the program

if __name__ == "__main__":
    main()
