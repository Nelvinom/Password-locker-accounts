import unittest
from user import Credentials


class TestCredentials(unittest.TestCase):


    def setUp(self):
        self.new_credentials = Credentials("aligedi","instagram","ali","aligedi")

    def tearDown(self):
        Credentials.credentials_list = []


    def test_init(self):


        self.assertEqual(self.new_credentials.view_passward,"aligedi")
        self.assertEqual(self.new_credentials.account,"instagram")
        self.assertEqual(self.new_credentials.login,"ali")
        self.assertEqual(self.new_credentials.passward,"aligedi")

    def test_save_credential(self):

        self.new_credentials.save_credential()
        self.assertEqual(len(Credentials.credentials_list),1)
    def test_multiple_credential(self):


        self.new_credentials.save_credential()
        self.test_credentials = Credentials("osmanhared","instagram","osman","osmanhared")
        self.test_credentials.save_credential()
        self.assertEqual(len(Credentials.credentials_list),2)

    def test_del_credential(self):


        self.new_credentials.save_credential()
        self.test_credentials = Credentials("osmanhared","instagram","osman","osmanhared")
        self.test_credentials.save_credential()
        self.new_credentials.del_credential()
        self.assertEqual(len(Credentials.credentials_list),1)
        
    def test_display_credential(self):

        self.assertEqual(Credentials.display_credentials(),Credentials.credentials_list)
    
    def test_exist_credential(self):


        self.new_credentials.save_credential()
        self.test_credentials = Credentials("osmanhared","instagram","osman","osmanhared")
        self.test_credentials.save_credential()

        credential_exists = Credentials.find_by_account("instagram")
        self.assertTrue(credential_exists)

if __name__ == '__main__':
    unittest.main()
