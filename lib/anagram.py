# your code goes here!
class Anagram:
    def __init__(self, word):
        self._word = word

    @property
    def word(self):
        return self._word
    
    @word.setter
    def word(self, value):
        if isinstance(value, str):
            self._word = value.lower()
        else:
            raise ValueError("Word must be a string")    
        
    def match(self, words):
        word_list = []
        for a in words:
            if sorted(a.lower()) == sorted(self._word):
                word_list.append(a)
        return word_list
            
