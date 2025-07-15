from string import ascii_letters, digits

class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False

        accepted_symbols = set(ascii_letters + digits)

        if set(word) - accepted_symbols:
            return False

        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}

        if not any(symbol in vowels for symbol in word):
            return False

        consonants = set(ascii_letters) - vowels

        if not any(symbol in consonants for symbol in word):
            return False

        return True
