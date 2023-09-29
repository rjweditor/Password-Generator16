# Password-Generator16

A password generator that generates passwords that would take over a trillion years to crack. 

```markdown
# Random Password Generator

This Python script generates a random password of 16 characters with the following requirements:

- At least 1 lowercase letter
- At least 1 uppercase letter
- At least 1 special character
- At least 1 number

## Getting Started

### Prerequisites

- Python 3.x (https://www.python.org/downloads/)

### Usage

1. Clone or download this repository to your local machine.

2. Open a terminal or command prompt.

3. Navigate to the directory containing the script.

4. Run the script using Python:

   ```bash
   python pass-gen-16.py
   ```

5. The script will generate a random password and display it in the terminal.

## How It Works

The `generate_password` function in the script follows these steps to create a random password:

1. Selects at least one character from each character set (lowercase, uppercase, special characters, and numbers).

2. Generates the remaining characters with random selections from all character sets.

3. Shuffles the characters to randomize the password.

## Example

Here's an example of a generated random password:

```
Random Password: R$5TgHj2qoD+p1Kx
```
<img width="633" alt="Screenshot 2023-09-28 at 10 21 06 PM" src="https://github.com/rjweditor/Password-Generator16/assets/13291967/4df5c0bd-0f70-460b-baf0-0c3829a28311">

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- The script uses Python's `random` module to generate random characters.
- The character sets for lowercase letters, uppercase letters, special characters, and numbers are predefined.

```
