# your code goes here!

class Anagram:
    def __init__(self, word):
        self.word = word.lower()
        self.sorted_word = sorted(self.word)

    def match(self, letters):
        anagrams = []
        for letter in letters:
            if sorted(letter.lower()) == self.sorted_word:
                anagrams.append(letter)
        return anagrams
    
    listen = Anagram("listen")

    listen.match(['enlist', 'google','inlets','banana'])