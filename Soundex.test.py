import unittest
from Soundex import generate_soundex

class TestSoundex(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(generate_soundex(""), "0000")

    def test_single_character(self):
        self.assertEqual(generate_soundex("A"), "A000")

    
if __name__ == '__main__':
    unittest.main()
