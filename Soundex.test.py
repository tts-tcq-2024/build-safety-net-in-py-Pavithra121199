import unittest
from Soundex import generate_soundex

class TestSoundex(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(generate_soundex(""), "0000")
    def test_single_character(self):
        self.assertEqual(generate_soundex("A"), "A000")
    def test_random_name(self):
        self.assertEqual(generate_soundex("Radhakrishnan"),"R326")  
    def test_nonvowel_single_character(self):
        self.assertEqual(generate_soundex("X"), "X000")           
    def test_all_vowels(self):
        self.assertEqual(generate_soundex("aeiou"),"A000")        
    def test_similar_sound(self):
        self.assertEqual(generate_soundex("Quite"), "Q300")        
        self.assertEqual(generate_soundex("Quiet"), "Q300")       
    def test_non_alphabetic_padwithzeros(self):
        self.assertEqual(generate_soundex("A2B"), "A100")         
    def test_repeatingcharacters_vowelsignored(self):
        self.assertEqual(generate_soundex("APPLE"), "A140")   
    def test_consecutive_sameletters_letters_hwy_ignored(self):
        self.assertEqual(generate_soundex("HARRYPOTTER"), "H613")   
    def test_same_consecutivecode_separatedbyvowel(self):
        self.assertEqual(generate_soundex("HANUMAN"), "H555")       # Example with same consecutive code separated by a vowel - coded twice
    def test_same_consecutivecode_separatedbyhwy(self):
        self.assertEqual(generate_soundex("RGYQ"), "R200")         # Example with same consecutive code separated by 'h', 'w' or 'y'  - coded as a single number
             
if __name__ == '__main__':
    unittest.main()
