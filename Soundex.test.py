import unittest
from Soundex import generate_soundex

class TestSoundex(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(generate_soundex(""), "0000")

    def test_single_character(self):
        self.assertEqual(generate_soundex("A"), "A000")

    def testcases(self):
        self.assertEqual(generate_soundex("Radhakrishnan"),"R326")  #Random name more than 4 characters
        self.assertEqual(generate_soundex("X"), "X000")            # Single character non-vowel pad with zeros
        self.assertEqual(generate_soundex("aeiou"),"A000")         # All vowels
        self.assertEqual(generate_soundex("Quite"), "Q300")        
        self.assertEqual(generate_soundex("Quiet"), "Q300")        # Similar sound 
        self.assertEqual(generate_soundex("A2B"), "A100")         # Non-alphabetic and pad with zeros
        self.assertEqual(generate_soundex("HARRYPOTTER"), "H613") # Example with same consecutive letters, containing vowels and 'hwy' which should be ignored other than 1st letter 
        self.assertEqual(generate_soundex("HANUMAN"), "H555")     # Example with same consecutive code separated by a vowel - coded twice
        self.assertEqual(generate_soundex("RGYQBAF"), "R211")     # Example for the rule two letters with the same number separated by 'h', 'w' or 'y' are coded as a single number,
                                                                  # whereas such letters separated by a vowel are coded twice. 
                                                                  #[ G and Q have the same code 2 separated by 'Y'=> coded once] [B and F have the same code 1 separated by a vowel 'A' => coded twice]
        
if __name__ == '__main__':
    unittest.main()
