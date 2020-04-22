class User:
    """
    Class that generates new instance of a user login.
    """

    user_list = []

    def __init__(self, first_name, last_name, password):

        self.first_name = first_name
        self.last_name = last_name
        self.password = password
