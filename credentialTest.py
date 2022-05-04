import unittest

from credential import Credential


class TestCredential(unittest.TestCase):

    def setUp(self):
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
         testCredential = Credential("swee","5648Y","instagram")
         testCredential.saveCredential()

         foundAccount = Credential.findByPassword("5648Y")
         self.assertTrue(foundAccount)

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