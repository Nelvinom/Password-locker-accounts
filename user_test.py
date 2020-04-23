import unittest
from user import User

class Testuser(unittest.TestCase):

    def setUp(self):
        self.new_user = User("Nelvin","123young")


    def tes_init(sef):


        self.assertEqual(self.new_user.username,"Nelvin")
        self.assertEqual(self.new_user.passward,"123young")

    def test_save_user(self):



        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)

    def test_user_exists(self):

        self.new_user.save_user()
        test_user = User("User","0712345")
        test_user.save_user()
        user_exists = User.user_exists("0712345")
        self.assertTrue(user_exists)
    
if __name__ == '__main__':
    unittest.main()

