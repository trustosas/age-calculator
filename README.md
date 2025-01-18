# Age Calculator

A simple script that calculates the time you've lived for.

## Description

The `age-calculator` repository contains a Python script, `age calculator (precise).py`, which calculates the precise duration of time you have lived, down to the minute. The script takes your birthdate (and optionally, your birthtime) to compute this information.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/trustosas/age-calculator.git
    ```
2. Navigate to the repository directory:
    ```sh
    cd age-calculator
    ```
3. Install the required dependencies:
    ```sh
    pip install python-dateutil
    ```

## Usage

1. Open the `age calculator (precise).py` file in a text editor.
2. Enter your birthdate in the `birthday` variable in the format `DD-MM-YYYY`.
    ```python
    birthday = '4-8-2001'
    ```
3. (Optional) Enter your birthtime in the `birthtime` variable in the format `HH:MM` (24-hour format). If you do not provide this information, the script will assume you were born at 00:00 (midnight).
    ```python
    birthtime = '14:30'  # Example: 2:30 PM
    ```
4. Run the script:
    ```sh
    python "age calculator (precise).py"
    ```
5. The script will output the current date and time along with the precise duration you have lived.

## Example Output
```
The current date & time is 2025-01-18 14:05:47
You've lived for 23 years, 4 months, 14 days and 5 hours
```

## License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](https://github.com/trustosas/age-calculator/blob/main/LICENSE) file for details.

## Author

- GitHub: [trustosas](https://github.com/trustosas)

Feel free to contribute to this project by submitting issues or pull requests. Enjoy calculating the precise time you've lived for!
