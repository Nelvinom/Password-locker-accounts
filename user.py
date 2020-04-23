class User:

    user_list = []

    def __init__(self, first_name, password):

        self.first_name = first_name
        self.password = password

    def save_user(self):
        User.user_list.append(self)

    
if __name__ == '__main__':
    main()