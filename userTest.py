import unittest

from user import User 

from credential import Credential



class TestUser(unittest.TestCase):

     #setup for testing
    def setUp(self):
        self.newUser = User("Michael","Junior","micjun2gmail.com","mics")
    
    #method to empty userlist for
    def tearDown(self):
        User.userList = []

    #check initialization
    def test_init(self):
        self.assertEqual(self.newUser.fName,"Michael")
        self.assertEqual(self.newUser.lName,"Junior")
        self.assertEqual(self.newUser.email,"micjun2gmail.com")
        self.assertEqual(self.newUser.username,"mics")

    def testsaveUser(self):
        self.newUser.saveUser()
        self.assertEqual(len(User.userList),1)

    def testsaveMultipleUsers(self):
        self.newUser.saveUser()
        testUser = User("Test","user","testuser@org","cheeks")
        testUser.saveUser()
        self.assertEqual(len(User.userList),2)


    def testdeleteUser(self):
        self.newUser.saveUser()
        testUser = User("Test","user","testuser@org","cheeks")
        testUser.saveUser()

        self.newUser.deleteUser()
        self.assertEqual(len(User.userList),1)

    def testfindByUsername(self):
        self.newUser.saveUser()
        testUser = User("Test","user","testuser@org","cheeks")
        testUser.saveUser()

        foundUser = User.FindByUsername("cheeks")

        self.assertEqual(foundUser.email,"testuser@org")


    def testuserExists(self):
        self.newUser.saveUser()
        testUser = User("Test","user","testuser@org","cheeks")
        testUser.saveUser()

        userExists = User.userExists("cheeks")

        self.assertTrue(userExists)

    def testdisplayUsers(self):
        self.assertEqual(User.displayUsers(),User.userList)


    


class TestCredential(unittest.TestCase):

    def SetUp(self):
        self.newCredential = Credential("cheeks","78456@","Twitter")

    def tearDown(self):
        Credential.credentialList = []

    def test_init(self):
        self.assertEqual(self.newCredential.username, "cheeks")
        self.assertEqual(self.newCredential.password, "78456@")
        self.assertEqual(self.newCredential.account,"Twitter")

    def testsaveCredential(self):
        self.newCredential.saveCredential()

        self.assertEqual(len(Credential.credentialList),1)


    def testsaveMultipleCredential(self):
        self.newCredential.saveCredential()
        testCredential = Credential("swee","5648Y","instagram")
        testCredential.saveCredential()

        self.assertEqual(len(Credential.credentialList),2)


    def testdeleteCredential(self):
        self.newCredential.saveCredential()
        testCredential = Credential("swee","5648Y","instagram")
        testCredential.saveCredential()

        testCredential.deleteCredential()
        self.assertEqual(len(Credential.credentialList),1)

    def testfindByPassword(self):
         self.newCredential.saveCredential()
         testCredential = Credential("swee","5648Y","instagram")
         testCredential.saveCredential()

         foundAccount = Credential.findByPassword("5648Y")
         self.assertTrue(foundAccount,testCredential.password)

    def testaccountExists(self):
         self.newCredential.saveCredential()
         testCredential = Credential("swee","5648Y","instagram")
         testCredential.saveCredential()

         accountCredentials = Credential.accountExists("swee")
         self.assertTrue(accountCredentials)

    def testdisplayCredential(self):
        self.assertEqual(Credential.displayCredential(),Credential.credentialList)







if __name__ == "__main__":
    unittest.main()