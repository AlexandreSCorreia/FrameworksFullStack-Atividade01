import unittest
import requests

class TestStringMethods(unittest.TestCase):

    def test_00_media(self):
        r1 = requests.get("http://localhost:5000/?nota1=6&nota2=7")
        if "6.5" not in r1.text:
            self.fail("a média de 6 com 7 deveria ter dado 6.5")

def runTests():
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestStringMethods)
    unittest.TextTestRunner(verbosity=2, failfast=True).run(suite)

runTests()