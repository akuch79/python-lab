from utils import square, is_even, celsius_to_fahrenheit


def main():
    number = float(input("Enter a number: "))

    print("Square:", square(number))
    print("Even:", is_even(number))
    print("Fahrenheit:", celsius_to_fahrenheit(number))


if __name__ == "__main__":
    main()
