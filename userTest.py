import unittest

from user import User 

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

        foundUser = User.findByUsername("cheeks")

        self.assertEqual(foundUser.email,"testuser@org")


    def testuserExists(self):
        self.newUser.saveUser()
        testUser = User("Test","user","testuser@org","cheeks")
        testUser.saveUser()

        userExists = User.userExists("cheeks")

        self.assertTrue(userExists,testUser.username)

    def testdisplayUsers(self):
        self.assertEqual(User.displayUsers(),User.userList)



if __name__ == "__main__":
    unittest.main()