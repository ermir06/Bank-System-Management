# Bank Management System

This Python project implements a simple Bank Management System. It allows users to create a bank account, log in, deposit money, withdraw money, view account balance, and exit the program.


## Files

The project consists of three Python files, `project.py`, `test_project.py` and `project_db.csv`.

### The file `project.py` contains the following sections:

1. Import Statements:
   - Imports necessary modules and libraries such as `re`, `csv`, `sys`, `pyttsx3`, `date` from `datetime`, `NamedTemporaryFile` and `shutil` from `tempfile`.

2. Global Variables:
   - `username2`, `password2`, and `balance` are used to store the current user's username, password, and balance, respectively.

3. `update_db()` Function:
   - Updates the account balance in the CSV database file (`project_db.csv`) after a deposit or withdrawal.

4. `Account` Class:
   - Represents a user account and provides methods to gather user information during account creation.

5. Helper Functions:
   - `deposit(money)`, `withdraw(money)`, and `return_balance(balance)` modify and retrieve the account balance.

6. `main()` Function:
   - Entry point of the program that displays the home page and handles account creation and login processes.

7. `create_account()` Function:
   - Creates a new bank account by collecting user information and storing it in the `project_db.csv` file.

8. `login_option()` Function:
   - Prompts the user to enter their username and password and verifies them against the data in `project_db.csv`.

9. `after_login()` Function:
   - Displays options to the user after login: deposit money, withdraw money, view balance, or exit the program.

10. `home_page()` Function:
    - Displays the Bank Management System home page with options to create an account or log in.

### The file `project_db.csv` contains the following sections:

1. Header: Full Name,Username,Password,Phone Number,Birthday,Balance

## Design Choices

The project uses a CSV file (`project_db.csv`) as a simple database to store account information.

The project aims to provide a user-friendly interface for banking operations while adhering to good coding practices.
