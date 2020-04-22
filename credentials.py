class Credentials:

    """
    class that generates new instances of credentials_list = users credentials
    """

    def __init__(self, credentials_name,credentials_password):
          self.credentials_name = credentials_name
          self.credentials_password = credentials_password

    credentials_list = []