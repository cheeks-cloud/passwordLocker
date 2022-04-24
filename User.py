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
  def findByLastName(cls,username):
    for user in cls.userList:
      if user.username == username:
        return user


  # @classmethod
  # def userExists(cls,lName):
  #   for user in cls.userList:
  #      if user.lName = lName:
  #          return True

  #      return False

  # @classmethod
  # def displayUsers(cls):
  #   return cls.userList

  # @classmethod
  # def copyEmail(cls,lName):
  #   userFound = lName.findByLastName(lName)
  #   pyperclip.copyEmail(userFound.email)







if __name__ == "__main__":
  main()
     
