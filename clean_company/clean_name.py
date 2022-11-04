from clean_company.helpers import *


class company:
    def __init__(self,word):
        self.word = word

    def clean(self):
        cleaned = clean_company(self.word)
        return cleaned