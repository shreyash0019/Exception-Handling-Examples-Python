# ATM Application with Exception Handling

This repository demonstrates exception handling in Python with a simple ATM application. The project showcases how to manage common issues like invalid PIN entries and withdrawing more money than the available balance using custom exception handling.

## Features

- **User Authentication**: Validate the user's PIN.
- **Check Balance**: Display the current account balance.
- **Withdraw Money**: Handle withdrawal requests with checks for sufficient funds.
- **Deposit Money**: Update the balance when money is deposited.
- **Custom Exceptions**: Examples of handling invalid PINs and insufficient balance scenarios.
- **Match-Case Statements**: Utilized to simplify menu operations and improve code readability.

## Example Exceptions Covered

1. **Invalid PIN**: Raised when the user enters an incorrect PIN.
2. **Insufficient Balance**: Raised when the withdrawal amount exceeds the available balance.

## Getting Started

### Prerequisites

- Python 3.x installed on your system.

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/Exception-Handling-Examples-Python.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Exception-Handling-Examples-Python
   ```

### Usage

1. Run the main script:
   ```bash
   python ATMOperationsMain.py
   ```
2. Follow the prompts to:
   - Enter your PIN.
   - Check your balance.
   - Withdraw or deposit money.

### Example Output

#### Case 1: Invalid PIN
```text
Enter your PIN: 1234
InvalidPINException: The entered PIN is incorrect.
```

#### Case 2: Insufficient Balance
```text
Enter your PIN: 5678
Enter amount to withdraw: 500
InsufficientBalanceException: Withdrawal amount exceeds available balance.
```

#### Case 3: Successful Transaction
```text
Enter your PIN: 5678
Enter amount to withdraw: 100
Transaction successful! Remaining balance: 900
```

## Project Structure

```
ATM Application
├── ATMOperations.py      # Contains core ATM operations logic
├── ATMOperationsMain.py  # Entry point of the application
├── AtmExcpt.py           # Custom exception classes
├── AtmMenu.py            # Menu handling using match-case statement
└── README.md             # Project documentation
```

## Custom Exceptions

### `InvalidPINException`
Raised when the user enters an incorrect PIN.

### `InsufficientBalanceException`
Raised when the withdrawal amount exceeds the available balance.

## Contributing

Contributions are welcome! Feel free to fork the repository and submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any questions or feedback, feel free to reach out:

- **Name**: Shreyash Ingle
- **Email** :ingleshreyas01@example.com

