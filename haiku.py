#for db
import sqlite3
import os
#to link db file location with python script location
path = os.path.dirname(os.path.realpath(__file__))
DB_LOCATION = os.path.join(path, "nini.db")
# for syllable counting feature
from nltk.corpus import cmudict
d = cmudict.dict()
import string
translator = str.maketrans('', '', string.punctuation)

def main():
    return write_haiku()

def write_haiku():
    """Guide user to write a haiku with a series of prompts. Syllable-count check will be performed. Haiku will be returned as formatted string (format == 3 lines)."""
    haiku = ""
    #Verse 1: place, 5 syllables
    prompt = " Think of a specific place: it could be your favorite place in the world, or the place where you have been the happiest in your life, or another particular place that has a special meaning for you. Please enter below a very short description of this place, or just one part of it.\nYour description needs to have a length of five syllables, when spoken out loud. It is okay to use your fingers to count! Examples of five-syllable descriptions of a place are: 'By a mountain lake', 'Copacabana', 'My mother's garden'.\nYour turn!"
    numsyl = 5
    haiku += get_verse(prompt, numsyl)
    #Verse 2: something changes, 7 syllables
    prompt = "Now, imagine yourself in this place, which you know so well. Look around, visualize all the details. Remember what makes this place special for you, specifically. Then, please describe a change: any type of change, anything that happens, or has happened, to this place, or at this place, to you, to someone else, to no one at all.\nThis time, you have seven syllables! Examples of a seven-syllable description of a change are: 'Dark grey clouds fill up the sky', 'The waitress folds her apron', 'Overgrown weeds everywhere'.\nYour turn!"
    numsyl = 7
    haiku += "\n" + get_verse(prompt, numsyl)
    #Verse 3: a sensation, 5 syllables
    prompt = "Finally, having visualized this special place, and described a change that happens or happened in relation to it, imagine how someone might have felt, witnessing that change, while being in that place. Describe a feeling, a thought, a sensation, which come as a response to that change.\nYou only have five syllables! Examples of a five-syllable description of a feeling, sensation, or thought, are: 'Suddenly I'm cold', 'Another cocktail?', 'How tired one gets'.\nYour turn!"
    numsyl = 5
    haiku += "\n" + get_verse(prompt, numsyl)
    print("Congratulations! Here is your very own haiku:\n\n"+haiku+"\n\nPlease, take some time to read it again. Forget about counting syllables, now. Just visualize once more the three miniature moments that you have come up with. Can you see something happening in these very few words? Does this something have any meaning to you? Could it have meaning to someone else? Or would you rather not have wasted your time writing three lines which really, really couldn't mean anything interesting? — If so, please feel free to email a copy of your haiku to nini-haikus@cumulus.cool and you will receive a third-party analysis within 5 business days, which may or may not support your assessment. — You may also read other haikus from our open anthology (see below) or check out the examples provided in our technical white paper.")
    option = opt_in_antho(haiku)
    if option:
        read_antho()
    else:
        return

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

def opt_in_antho(haiku):
    """Option to add the haiku to an open anthology"""
    print("OPTIONAL: Would you like to add your haiku to our open anthology, so that others may read it? If so, please enter 'yes' below, then you may add your name and today's date. Otherwise, just press Enter to move on.\n--Please note: users who submit a haiku are then given temporary access to read the anthology. Providing your name or pseudonym is not required. You agree to this use of your haiku, and release me from any liability regarding your copyright as the author of your haiku. This is just a friendly experiment :)")
    choice = input()
    if choice == "":
        return False
    elif choice == "yes":
        print("Thanks for contributing!\nYou may now add your name or pseudonym: ")
        while True:
            author = input()
            if len(author) < 50:
                break
            else:
                print("Enter a valid name or pseudonym of less than 50 characters.")
        print("You may record today's date also:")
        while True:
            date = input()
            if len(date) < 50:
                break
            else:
                print("Enter a valid date.")
        with sqlite3.connect(DB_LOCATION) as con:
            cur = con.cursor()
            # create table if does not exist
            try:
                cur.execute("CREATE TABLE haikus(haiku_text, name, date)")
            except:
                pass
            # insert haiku data into db
            cur.execute("INSERT INTO haikus (haiku_text, name, date) VALUES (?, ?, ?)", (haiku, author, date))
            con.commit()
        print("Thank you! Your haiku has been recorded in the open anthology.")
        return True

def read_antho():
    """User can read haikus from anthology, after submitting one."""
    # get list of db entries
    with sqlite3.connect(DB_LOCATION) as con:
        cur = con.cursor()
        cur.execute("SELECT * FROM haikus")
        haikus = cur.fetchall()
    num = len(haikus)
    i = 0
    print(f"There are currently {num} haikus in the anthology. Please enter '1' to read one, or Enter to move on.")
    choice = input()
    while choice == "1" and i < num:
        print("\n\n"+haikus[i][0]+"\n\nAuthor: "+haikus[i][1]+"\nDate: "+haikus[i][2]+"\n")
        i += 1
        choice = input("Please enter '1' to read another haiku, or Enter to move on.")
    if choice == "1" and i == num:
        print("\nYou have read all the haikus available at this time. Thank you.\n")
    return

if __name__ == "__main__":
    main()
