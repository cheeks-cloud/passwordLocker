import pyperclip

class User:

  userList = []


  def __init__(self,fName,lName,email,username):
    self.fName = fName
    self.lName = lName
    self.email = email
    self.username = username
    
                                                #saving a new user 

  def saveUser(self):
    User.userList.append(self)


                                        #method to delete an existing user
  def deleteUser(self):
    User.userList.remove(self)

                                         #method to find a user using their username
  @classmethod  
  def findByUsername(cls,username):
    for user in cls.userList:
      if user.username == username:
        return user

                                         #method to check whether a user exists 
  @classmethod
  def userExists(cls,email):
    for user in cls.userList:
       if user.email == email:
           return True

       return False

                                            #method to display all users      

  @classmethod
  def displayUsers(cls):
    return cls.userList

                                               #method to copy and paste

  @classmethod
  def copyEmail(cls,username):
    userFound = username.findByUsername(username)
    pyperclip.copyEmail(userFound.email)





if __name__ == "__main__":
  main()
     
