from credential import Credential
from user import User

create a new user 

def createUser(fName, lName, email,username):
  newUser = User(fName,lName,email,username)
  return newUser

def saveUser(user):
  user.saveUser()

def deleteUser(user):
  user.deleteUser()

def userExists(user):
  return  User.exists(user)

def displayUsers():
  return User.displayUsers()

# # def find

# def createCredential(username, password,account):
#   newCredential = Credential(username, password, account)
#   return newCredential

# def saveCredential(credential):
#   credential.saveCredential()

# def deleteCredential(credential):
#    credential.deleteCredential()

# def accountExists(account):
#   return 


