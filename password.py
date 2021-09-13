class User:
  '''
  Class that generates new instances of user
  '''
  user_details = []

  def __init__ (self,first_name,last_name,phone_number,email):
    '''
    __init__ method that helps define properties
    
    Args: 
        first_name: User's first name
        last_name: User's last name
        phone_number: User's phone number
        email: User's email address
    '''
    self.first_name = first_name
    self.last_name = last_name
    self.phone_number = phone_number
    self.email = email

  def save_user_information(self):
    '''
    save_user_information methods adds new user information at the end of the list
    '''
    User.user_details.append(self)

  def delete_user(self):
    '''
    delete_user method removes previously saved user from the list
    '''
    pass