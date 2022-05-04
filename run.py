#!/usr/bin/env python3.8

from credential import Credential
from user import User



def createUser(fName, lName, email,username):
  newUser = User(fName,lName,email,username)
  return newUser

def saveUser(user):
  User.saveUser(user)

def deleteUser(user):
  User.deleteUser(user)

def userExists(username):

  return  User.userExists(username)

def displayUsers():
  return User.displayUsers()

def findUByUsername(username):
  return User.findByUsername(username)


def createCredential(username, password,account):
  newCredential = Credential(username, password, account)
  return newCredential

def saveCredential(credential):
  Credential.saveCredential(credential)

def deleteCredential(credential):
   Credential.deleteCredential(credential)

def accountExists(username):
  return Credential.accountExists(username)

def displayCredential():
  return Credential.displayCredential()

def findCredential(password):
  return Credential.findByPassword(password)

def main():
   print("Hello Welcome to your Pasword Locker Account. What is your name?")
   username = input()   
   print(f"Hello {username}. what would you like to do?")
   print('\n')

  #  saveUser(createUser(fName,lName, username , email))

   while True:
      print("Use these short codes : cc - create a new user , dc - display users, fc -find a user,mc - display credentials,dl - delete a user ex -exit ")
      short_code = input().lower()    
      if short_code == 'cc':
            print("Enter the users credentials")
            print("-"*10)
            print ("First name is:")
            fName = input()

            print("Last name:")
            lName = input()

            print("Username:")
            username = input()

            print("Email address:")
            email = input()

            print("Enter username for site your creating password for:")
            username = input()

            print("Enter password:")
            password = input()

            print("Enter account:")
            account = input()

            saveUser(createUser(fName,lName, username , email))

            saveCredential(createCredential(username, password, account))

            print ('\n')
            print(f"New User {fName} {lName} created")
            print ('\n')

      elif short_code == 'dc':
          if displayUsers():
            print("Here is a list of all your Users")
            print('\n')

            for user in displayUsers():
              print(f'{user.fName}   {user.lName} {user.email}')
              print("\n")
          
          else:
              print('\n')
              print("You dont seem to have any Users saved yet")
              print("\n")

      elif short_code == 'mc':
          if displayCredential():
            print("Here is a list of all your credentials")
            print('\n')

            for credential in displayCredential():
              print(f'{credential.username}   {credential.password} {credential.account}')
              print('\n')

          else:
                print('\n')
                print("You dont seem to have any credential saved yet")
                print("\n")


      elif short_code == 'fc':
          print("Enter the username you want to search for")

          searchuser = input()

          if userExists(searchuser):
            searchUser = userExists(searchuser)
            print(f' The user is:{searchUser.fName}   {searchUser.lName}')
            print('-' * 20)
            print(f'Their Email address:{searchUser.email}')
          else:
            print("That user does not exist")


      elif short_code == 'ex':
        print('Bye....')
        break
      else:
        print("Please use short codes")
              



if __name__ == '__main__':

    main()
                                                                                                          

                                               