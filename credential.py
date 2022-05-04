import random



class Credential:

  credentialList = []


  def __init__(self,account,username,password):
    self.username = username
    self.password = password
    self.account = account

                                             #save credentials

  def saveCredential(self):
    Credential.credentialList.append(self)

                                              #delete credentials

  def deleteCredential(self):
    Credential.credentialList.remove(self)


                                          #find using password

  @classmethod
  def findByPassword(cls,password):

    for credential in cls.credentialList:
      if credential.password == password:
        return password



                                                  #check if credentials exist
  @classmethod
  def accountExists(cls,username):
    for credential in cls.credentialList:
      if credential.username == username:
        return True

      return False

                                          #display all credentials
  @classmethod
  def displayCredential(cls):
    return cls.credentialList






