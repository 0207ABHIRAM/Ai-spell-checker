import nltk
from nltk.corpus import words
from difflib import get_close_matches
from src.preprocess import clean_text

nltk.download('words')

class SpellChecker:
    def __init__(self):
        self.word_list = set(words.words())

    def correct_word(self, word):
        matches = get_close_matches(word, self.word_list, n=1, cutoff=0.8)
        return matches[0] if matches else word

    def correct_sentence(self, sentence):
        cleaned = clean_text(sentence)
        tokens = cleaned.split()
        corrected_tokens = [self.correct_word(word) for word in tokens]
        return ' '.join(corrected_tokens)
