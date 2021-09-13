import unittest
from password import User

class TestUser(unittest.TestCase):
  '''
  Test class that defines test cases for the user class behaviours.
  Args:
      unnittest.TestCase: TestCase class that helps in creating test cases
  '''
  def setUp(self):
    '''
    Set up method to run before each test case
    '''
    self.new_user = User("Harry","Bett","0711223344","hb@ms.com")

  def test_init(self):
    '''
    test_init test case to test if the object is initialized properly
    '''

    self.assertEqual(self.new_user.first_name, "Harry")
    self.assertEqual(self.new_user.last_name, "Bett")
    self.assertEqual(self.new_user.phone_number, "0711223344")
    self.assertEqual(self.new_user.email, "hb@ms.com")

  def test_save_user (self):
    '''
    test_save_contact test case to test if the user object is saved into the user details list
    '''
    self.new_user.save_user_information()
    self.assertEqual(len(User.user_details), 1)

  def tearDown(self):
    '''
    tearDown method that does clean up after each test case has run
    '''
    User.user_details = []

  def test_save_multiple_user(self):
    '''
    test_save_multiple_user to check if we can save mutiple user objects to the user details list
    '''
    self.new_user.save_user_information()
    test_user = User("John","doe","0712345678","jd@ms.com")
    test_user.save_user_information()
    self.assertEqual(len(User.user_details), 2)

  def test_delete_user(self):
    '''test_delete_user to test if we can remove user from a user list
    '''
    self.new_user.save_user_information()
    test_user = User("John", "doe", "0712345678", "jd@ms.com")
    test_user.save_user_information()

    self.new_user.delete_user()
    self.assertEqual(len(User.user_details), 1)
    

if __name__ == '__main__':
  unittest.main()