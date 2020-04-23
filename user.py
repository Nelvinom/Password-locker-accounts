class User:

    user_list = []

    def __init__(self, first_name, password):

        self.first_name = first_name
        self.password = password

    def save_user(self):
        User.user_list.append(self)

    @classmethod
    def user_exists(cls, character):
        for user in cls.user_list:
            if user.password == character:
                return True

        return False

    @classmethod
    def find_by_first_name(cls, name):
        for user in cls.user_list:
            if user.first_name == name:
                return True

        return False


class Credentials:
    credentials_list = []

    def __init__(self, view_password, account, login, password):
        self.view_passward = view_password
        self.account = account
        self.login = login
        self.password = password

    def save_credential(self):
        Credentials.credentials_list.append(self)

    def del_credential(self):
        Credentials.credentials_list.remove(self)

    @classmethod
    def display_credentials(cls):
        return cls.credentials_list

    @classmethod
    def find_by_account(cls, account):
        for creden in cls.credentials_list:
            if creden.account == account:
                return creden
        return False

    @classmethod
    def credentials_exist(cls, view_passward):
        for creden in cls.credentials_list:
            if creden.view_password == view_password:
                return True
        return False
