
# class Credential:

#   credentialList = []


#   def __init__(self,account,username,password):
#     self.username = username
#     self.password = password
#     self.account = account

#                                               #save credentials

#   def saveCredential(self):
#     Credential.credentialList.append(self)

#                                               #delete credentials

#   def deleteCredentials(self):
#     Credential.credentialList.remove(self)


                                          #generatePassword

  # def generatePassword(self, size = 6, char=strings.ascii_uppercase +
  # ascii_lowercase + string.digits):

  #    passGiven = ''.join(random.choice(char)for _ in range(size))  

  #    return passGiven


  #                                            #find using password

  # @classmethod
  # def findByCredentials(cls,password):

  #   for credential in cls.credentialList:
  #     if credential.password == password:
  #       return account



  #                                                 #check if credentials exist
  # @classmethod
  # def passwordExists(cls,password):
  #   for credential in cls.credentialList:
  #     if credential.password == password:
  #       return True

  #     return False

  #                                         #display all credentials
  # @classmethod
  # def displayCredential(cls):
  #   return cls.credentialList





# if __name__ == "__main__":
#   main()