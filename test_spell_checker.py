import unittest
from src.spell_corrector import SpellChecker

class TestSpellChecker(unittest.TestCase):
    def test_correct_sentence(self):
        checker = SpellChecker()
        result = checker.correct_sentence("Ths is a splel cheker")
        self.assertEqual(result, "this is a spell checker")

if __name__ == '__main__':
    unittest.main()
