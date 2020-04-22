import unittest
from credentials import Credentials

class TestCredentials(unittest.TestCase):

  
 def setUp(self):
        
        self.new_credentials = Credentials("facebook","1234") # create credential object


 def tearDown(self):
        
        Credentials.credentials_list = []

 def test_credentials_instance(self):

        
        self.assertEqual(self.new_credentials.credentials_name,"facebook")
        self.assertEqual
        (self.new_credentials.credentials_password,"1234")
 def test_save_credentials(self):
        
        self.new_credentials.save_credentials()
        self.assertEqual(len(Credentials.credentials_list),)
 def test_delete_credentials(self):
        
        self.new_contact.save_contact()
        test_contact = Contact("Test","user","0712345678","test@user.com") # new contact
        test_contact.save_contact()

        self.new_contact.delete_contact()# Deleting a contact object
        self.assertEqual(len(Contact.contact_list),1)
if __name__ == '__main__':
    unittest.main()