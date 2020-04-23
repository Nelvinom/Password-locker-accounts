#!/usr/bin/env python3.6

import random
from user import User
from user import Credentials


def create_user_account(user_name, pass_word):
    new_user = User(user_name, pass_word)
    return new_user


def save_user_account(user):
    user.save_user()


def check_existing_user(character):
    return User.user_exists(character)


def create_credentials(view_password, account, login_name, pass_word):
    new_credential = Credentials(view_password, account, login_name, pass_word)
    return new_credential


def save_credentials(credential):
    credential.save_credential()


def del_credential(Credentials):
    Credentials.del_credential()


def check_existing_credentials(account):
    return Credentials.credentials_exist(account)


def find_credential(account):
    return Credentials.find_by_account(account)


def display_credentials():
    return Credentials.display_credentials()


def main():
    print("Hello! Welcome to the Password Locking app. What is your name?")
    your_name = input().lower()
    print("\n")
    print(f"Hello {your_name}!! What would you like to check on?")
    while True:
        print("\nUse these short codes below:")
        print("-" * 30)
        print("\n ca - create an account, cc - create credentials, gp - generate password, cp - create own password, dc - display credentials, rc - delete credentials, ex - exit password locker")
        short_code = input()

        if short_code == 'ca':
            print("New account")
            print("-" * 30)

            print("\nEnter your user name")
            print("-"*40)
            user_name = input()

            print("\nEnter a password")
            print("-"*40)
            pass_word = input()

            save_user_account(create_user_account(user_name, pass_word))
            print("\n")
            print(f"New Account **{user_name}** created.\n")
        elif short_code == "cc":

            print("\nLogin to your account")
            print("-"*40)
            print("\nUsername?")
            print("-" * 20)
            user_name = input()

            print("\nPassword?")
            print("-"*15)
            user_password_input = input()

            view_password = user_password_input
            if check_existing_user(user_password_input):
                print("\nWelcome back!")
                print("New Credential")
                print("-" * 20)

                print("\nWhich account do the credentials belong to?")

                account = input()

                print(f"\nWhat's your login name for the {account} account?")

                login_name = input()

                print("\nchoose:")
                print("'gp' -  generate a  password , 'cp' - create your own password")
                password_creation_input = input()
                if password_creation_input == "cp":
                    print("\nEnter your password")
                    print("\n")
                    pass_word = input()
                elif password_creation_input == "gp":
                    chars = "abcdefghijklmnopqrstuvwxyz1234567890"
                    pass_word = "".join(random.choice(chars) for _ in range(8))
                    print(f"\nYour password is: **{pass_word}**")

                save_credentials(create_credentials(
                    view_password, account, login_name, pass_word))
                print("\n")
                print(f"New credentials created")

            else:
                print("Wrong password or username. Please Try again.\n Username?")
                print("-"*20)
                user_name = input()
                print("\nPassword?")
                print("-"*20)
                pass_word = input()
                if check_existing_user(user_password_input):
                    print("\nWelcome back!")
                else:
                    print("You don't have an account.\n")

        elif short_code == 'dc':

            if display_credentials():
                print("Here is a list of your credentials:")
                print("-"*40)

                for credential in display_credentials():
                    print(
                        f"\nAccount: {credential.account}\nLogin Name: {credential.login}\nAccount Password: {credential.passward}")
            else:
                print("\n You don't seem to have any credentials saved yet")

        elif short_code == 'rc':
            print("Enter the account name you want to delete")

            del_account = input()
            if check_existing_credentials(del_account):
                del_credential(find_credential(del_account))

                print(f"Deleted credentials of {del_account}")

            else:
                print("That credential does not exist")

        elif short_code == 'ex':
            print("-"*50)
            print("Thank you for using Password Locker...")
            print("-"*50)
            break

        else:
            print("Sorry, I didn't get that. Please use the short codes\n")


if __name__ == '__main__':
    main()
