import unittest
from translator import englishToFrench, frenchToEnglish

class TestfrenchToEnglish(unittest.TestCase):
    """ Test French to English """
    def testA(self):
        self.assertEqual(frenchToEnglish('0'), '0')
        self.assertNotEqual(frenchToEnglish(0), 0)
        self.assertEqual(frenchToEnglish('patisserie'), 'bakery')
        self.assertNotEqual(frenchToEnglish("None"), '')
        
class TestenglishToFrench(unittest.TestCase):
    """ Test Englisth to French"""
    def testB(self):
        self.assertEqual(englishToFrench('0'), '0')
        self.assertNotEqual(englishToFrench(0), 0)
        self.assertEqual(englishToFrench('bakery'), 'patisserie')
        self.assertNotEqual(englishToFrench("None"), '')
   
unnitest.main()