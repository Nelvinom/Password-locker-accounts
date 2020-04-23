import unittest
from user import User

class Testuser(unittest.TestCase):

    def setUp(self):
        self.new_user = User("ali","aligedi")


    def tes_init(sef):


        self.assertEqual(self.new_user.username,"ali")
        self.assertEqual(self.new_user.passward,"aligedi")

    def test_save_user(self):



        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)

    def test_user_exists(self):

        self.new_user.save_user()
        test_user = User("User","073645")
        test_user.save_user()
        user_exists = User.user_exists("073645")
        self.assertTrue(user_exists)
    
if __name__ == '__main__':
    unittest.main()

