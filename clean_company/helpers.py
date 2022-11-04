from cleanco import *
import re


def remove_firstlast(word,letter):
    if len(word) > 1:
        if word[0] == letter and word[-1] == letter:
            word = word[1:-1]
    return word

def clean_company(word):

    # Convert to uppercase
    cleaned = word.upper()
    # Remove start and last character if '
    cleaned = remove_firstlast(cleaned,"'")
    # Remove commas
    cleaned = cleaned.replace(',', '')
    # Remove hyphens
    cleaned = cleaned.replace(' - ', ' ')
    # Remove text between parenthesis and slash
    cleaned=re.sub(r"\(.*?\)","",cleaned)
    cleaned=re.sub(r"\\.*?\\","",cleaned)
    cleaned=re.sub(r"\/.*?\/","",cleaned)
    # Replace & with and
    cleaned = cleaned.replace(' & ', ' AND ')
    # Remove spaces in the begining/end
    cleaned = cleaned.strip()
    # Remove dots
    cleaned = cleaned.replace('.', '')
    cleaned = cleaned.replace('-', ' ')
    #Remove business entities extensions - after removing the dots
    cleaned = basename(cleaned)
    # Remove whitespaces
    cleaned = cleaned.strip()
    cleaned = cleaned.replace(r'\s+', ' ')
    # back to lowercase
    cleaned = cleaned.lower()

    return cleaned
