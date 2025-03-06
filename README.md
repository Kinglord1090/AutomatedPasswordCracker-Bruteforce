
# Automated Password Cracker [Bruteforce] 🔓

This project is a password cracking tool that automates the process of generating all possible password combinations from a predefined set of characters. It is designed for testing password strength by attempting to guess passwords of varying lengths, starting from a specified minimum to a maximum length. The tool utilizes a brute-force approach to try every combination and measures the time and number of guesses required to find the correct password.

## Features

- **Brute-Force Password Cracking**: The tool uses a brute-force algorithm to generate all possible combinations of a predefined set of characters to guess the password.
- **Customizable Password Length**: Users can specify the minimum and maximum lengths of the passwords to be generated, providing flexibility in testing different password complexities.
- **Predefined Character Set**: The password generation is based on a list of 100 keyboard characters, including digits, uppercase and lowercase letters, and special characters, mimicking real-world password patterns.
- **Real-Time Password Guessing**: As the program runs, it displays each password guess in real-time (except when the correct password is found), allowing users to track progress.
- **Password Cracking Metrics**: Once the correct password is found, the program reports the total number of guesses made, the time taken, and the cracking speed (guesses per second), giving users insight into the performance of the tool.
- **Error Handling**: The code includes basic input validation to ensure that users provide valid numbers for password lengths.
- **Extensibility**: The project is structured in a way that allows easy modification, such as adding more characters to the character set or altering the method of generating passwords.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/Kinglord1090/automated-password-cracker.git
    ```
2. Navigate to the project folder:
    ```bash
    cd automated-password-cracker
    ```

## Usage

1. Run the script:
    ```bash
    python auto-pass-cracker.py
    ```
2. The program will prompt you to enter the minimum and maximum lengths of the passwords to be generated.
3. Enter the desired password lengths, and the program will attempt to crack the hard-coded password.
4. If the password is found, it will display the result with the time taken and the number of guesses tried.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thanks to [itertools](https://docs.python.org/3/library/itertools.html) for providing the `product` function to generate combinations.
- Inspired by security best practices and password-strength testing tools.
