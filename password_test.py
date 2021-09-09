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