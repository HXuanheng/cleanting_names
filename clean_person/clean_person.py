from clean_person.helpers import *


class person:
    def __init__(self,word):
        self.word = word

    def name(self):
        cleaned = clean_person(self.word)[0]
        return cleaned
    
    def mid(self):
        cleaned = clean_person(self.word)[1]
        return cleaned

    def last(self):
        cleaned = clean_person(self.word)[2]
        return cleaned

    def title(self):
        cleaned = clean_person(self.word)[3]
        return cleaned

    def suffix(self):
        cleaned = clean_person(self.word)[4]
        return cleaned

    def roman(self):
        cleaned = clean_person(self.word)[5]
        return cleaned