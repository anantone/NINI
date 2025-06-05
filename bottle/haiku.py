from nltk.corpus import cmudict
d = cmudict.dict()
import string
translator = str.maketrans('', '', string.punctuation)

def get_verse(prompt, numsyl):
    """Returns a valid string, in terms of syllable count, in user response to prompt"""
    error_nsyl = "This does not seem to have the correct number of syllables. Try again!"
    success_nsyl = "Well done."
    print(prompt)
    string = input()
    while not check_nsyl(string, numsyl):
        print(error_nsyl)
        string = input()
    print(success_nsyl)
    return string

def check_nsyl(string, number):
    """checks if {string} has {number} of syllables"""
    #removes punctuation
    clean = string.translate(translator)
    #splits string into list of words
    lst_words = clean.split()
    #initialize string syllable count
    count = 0
    #iterate through list to count each word's syllables
    for word in lst_words:
        count += nsyl(word)
    #returns Boolean
    return True if ( count == number) else False

def nsyl(word):
    """For a given English word, return its number of syllables"""
    try:
        #from cmudict, a module of nltk: accurate, but relatively limited corpus
        result = [len(list(y for y in x if y[-1].isdigit())) for x in d[word.lower()]][0]
    except:
        #backup method based on vowel count: only accurate with words like "Chandigarh", which are often, but not always the ones not in cmudict!
        syllable_count = 0
        for w in word:
            if w == "a" or w == "e" or w == "i" or w == "o" or w == "u" or w == "A" or w == "E" or w == "I" or w == "O" or w == "U":
                syllable_count = syllable_count + 1
        result = syllable_count
    return result
