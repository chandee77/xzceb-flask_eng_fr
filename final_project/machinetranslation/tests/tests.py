import unittest
from translator import english_to_french, french_to_english

class TestFrenchToEnglish(unittest.TestCase):
    
    def test_null_input_english_to_french(self):
        result = english_to_french(None)
        self.assertIsNone(result)

    def test_null_input_french_to_english(self):
        result = french_to_english(None)
        self.assertIsNone(result)

    def test_english_to_french(self):
        result = english_to_french('Hello')
        self.assertEqual(result, 'Bonjour')
        
    def test_french_to_english(self):
        result = french_to_english('Bonjour')
        self.assertEqual(result, 'Hello')

if __name__ == '__main__':
    unittest.main()
