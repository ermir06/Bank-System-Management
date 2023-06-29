import re
import csv
import sys
import pyttsx3
from datetime import date
from tempfile import NamedTemporaryFile
import shutil



engine = pyttsx3.init()
username2 = ""
password2 = ""
balance = 0



def update_db():
    global balance

    tempfile = NamedTemporaryFile(mode="w", delete=False)

    fields = ["Full Name", "Username", "Password", "Phone Number", "Birthday", "Balance"]

    with open("project_db.csv", "r") as csvfile, tempfile:

        reader = csv.DictReader(csvfile, fieldnames=fields)
        writer = csv.DictWriter(tempfile, fieldnames=fields)

        for row in reader:
            if row["Username"] == username2 and row["Password"] == password2:
                print("Updating Balance", row["Balance"])
                        # New data
                new_data = [row["Full Name"], row["Username"], row["Password"], row["Phone Number"], row["Birthday"], balance]

                row["Full Name"], row["Username"], row["Password"], row["Phone Number"], row["Birthday"], row["Balance"] = new_data

            row = {
                    "Full Name": row["Full Name"],
                    "Username": row["Username"],
                    "Password": row["Password"],
                    "Phone Number": row["Phone Number"],
                    "Birthday": row["Birthday"],
                    "Balance": row["Balance"],
            }

            writer.writerow(row)


    shutil.move(tempfile.name, "project_db.csv")





class Account:

    @property
    def fullname(self):
        return self.fullname

    def get_fullname(self):
        fullname = input("Enter your Full Name: ")
        if re.search(r"^[a-zA-Z]+ [a-zA-Z]+", fullname):
            return fullname.title()
        else:
            return self.get_fullname()

    def get_username(self):
        username = input("Enter username: ")
        if re.search(r"^[a-zA-Z]+[a-zA-Z0-9]+$", username):
            return username
        else:
            print("Invalid username")
            return self.get_username()

    def get_password(self):
        password = input("Enter password: ")
        if re.search(r"^[a-zA-Z]+\w+$", password) and len(password) >= 8:
            return password
        else:
            print("Invalid password")
            return self.get_password()

    def get_Pnumber(self):
        phone_number = input("Enter your phone number: ")
        if re.search(r"^[0-9]+$", phone_number):
            return phone_number
        else:
            print("Invalid Phone Number")
            return self.get_Pnumber()

    def get_birthday(self):
        birthday = input("Date of Birth: ")
        try:
            date.fromisoformat(birthday)
            return birthday
        except:
            print("Invalid Birthday")
            return self.get_birthday()




def deposit(money):
    global balance
    balance += money
    update_db()
    return balance


def withdraw(money):
    global balance
    balance -= money
    update_db()
    return balance

def return_balance(balance):
    return balance



def main():
    option = int(home_page())
    global balance


    match option:
        case 1:
            create_account()
        case 2:
            print("\n\t\t**************************")
            print("\t\tLOGIN TO YOUR BANK ACCOUNT")
            print("\t\t**************************\n")

            option2 = 0

            if login_option() == True:
                option2 = after_login()

            if option2 == 1:
                money = int(
                    input("How much money you want to deposit to your bank account: ")
                )
                deposit(money)
                print(f"You have successfully depositet {money}$")



            elif option2 == 2:
                money = int(
                    input(
                        "How much money you want to withdraw from your bank account: "
                    )
                )
                withdraw(money)
                print(f"You have successfully withdraw {money}$")



            elif option2 == 3:
                print("Your account balance is:", return_balance(balance))

            elif option2 == 4:
                sys.exit("\nThank you for using our bank system\n")


def create_account():
    account = Account()
    fullname = account.get_fullname()
    username = account.get_username()
    password = account.get_password()
    phone_number = account.get_Pnumber()
    birthday = account.get_birthday()

    information = {
        "Full Name": fullname,
        "Username": username,
        "Password": password,
        "Phone Number": phone_number,
        "Birthday": birthday,
        "Balance": 0,
    }

    with open("project_db.csv", "a", newline="") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=[
                "Full Name",
                "Username",
                "Password",
                "Phone Number",
                "Birthday",
                "Balance",
            ],
        )
        writer.writerow(information)

        print("Account created successfully")
def login_option():

    global username2
    global password2
    global balance

    username = input("Enter Username: ")
    password = input("Enter Password: ")


    with open("project_db.csv") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["Username"] == username and row["Password"] == password:
                username2 = username
                password2 = password
                balance = int(row["Balance"])
                return True


        else:
            print("Invalid username or password")
            return login_option()


def after_login():
    print("1. Deposit money\n2. Withdraw money\n3. View balance\n4. Exit\n")

    #say
    engine.say("press 1 to deposit money, press 2 to withdraw money, press 3 to view your balance, press 4 to exit the program")
    engine.runAndWait()

    option = input("Enter your choice -> ")
    return int(option)



def home_page():
    print("\n\t\t**********************")

    print("\t\tBANK MANAGEMENT SYSTEM")

    print("\t\t**********************\n")

    print("1. Create Bank Account\n2. Login to your Bank Account")

    #say
    engine.say("Welcome to the Doni Bank, press 1 to create a new account, press 2 to login to your account")
    engine.runAndWait()



    option = input("\nEnter your choice -> ")

    return option


if __name__ == "__main__":
    main()
