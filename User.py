import pyperclip

class User:

  userList = []


  def __init__(self,fName,lName,email):
    self.fName = fName
    self.lName = lName
    self.email = email

  # def saveUser(self):
  #   User.userList.append(self)



  # def deleteUser(self):
  #   User.userList.remove(self)


  # @classmethod  
  # def findByLastName(cls,lName):
  #   for user in cls.userList:
  #     if user.lName = lName:
  #       return user


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
     
