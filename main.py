#for search feature
from search import search_w
#for haiku generation
from haiku import write_haiku
#for db
import sqlite3
import os
#to link db file location with python script location
path = os.path.dirname(os.path.realpath(__file__))
DB_LOCATION = os.path.join(path, "nini.db")
#for white paper
from rich.console import Console
from rich.markdown import Markdown
from pydoc import pager

def main():
    """This works as a command line menu to which the user returns after each task, until explicitly quitting."""
    #create db file if does not exist
    try:
        con = sqlite3.connect(DB_LOCATION)
        con.close()
    except:
        pass
    #Welcome page
    welcome_message = "\n\n---@@@    NINI  -  A NATURAL INTELLIGENCE ENABLER   @@@---\n\nWelcome! This prototype enables you to leverage Natural Intelligence for:\n\n- gathering information about a topic of your choice.\n- generating creative, structured, linguistic content.\n- suggesting further enablement modalities.\n\nNatural Intelligence can best be described as a past-generation form of A.I.: to learn more, please read our technically white paper (available after you've tried a feature, or two)."
    print(welcome_message)
    #Menu
    menu = "\nWhat would you like to do?\n\n1) Search for information\n2) Generate creative content\n3) Suggest a new feature\n\nPlease enter the number of your choice (or 'q' to quit): "
    white = 1
    #User's choice of task, or quit (complexities are for white paper joke!)
    task = input(menu)
    while task != "q":
        if white == 0:
            menu = "\nWhat would you like to do?\n1) Search for information\n2) Generate creative content\n3) Suggest a new feature\n4) Read our technically white paper\n\nPlease enter the number of your choice (or 'q' to quit): "
        elif white == 2:
            menu = "\nWhat would you like to do?\n1) Search for information\n2) Generate creative content\n3) Suggest a new feature\n4) Read our technical white paper again??\n\nPlease enter the number of your choice (or 'q' to quit): "
        if task == "1":
            search_w()
            if white == 1:
                white = 0
                menu = "\nWhat would you like to do?\n1) Search for information\n2) Generate creative content\n3) Suggest a new feature\n4) Read our technically white paper\n\nPlease enter the number of your choice (or 'q' to quit): "
            task = input(menu)
        elif task == "2":
            write_haiku()
            if white == 1:
                white = 0
                menu = "\nWhat would you like to do?\n1) Search for information\n2) Generate creative content\n3) Suggest a new feature\n4) Read our technically white paper\n\nPlease enter the number of your choice (or 'q' to quit): "
            task = input(menu)
        elif task == "3":
            get_suggestion()
            if white == 1:
                white = 0
                menu = "\nWhat would you like to do?\n1) Search for information\n2) Generate creative content\n3) Suggest a new feature\n4) Read our technically white paper\n\nPlease enter the number of your choice (or 'q' to quit): "
            task = input(menu)
        elif white == 0 and task == "4":
            read_whitely()
            white = 2
            menu = "\nWhat would you like to do?\n1) Search for information\n2) Generate creative content\n3) Suggest a new feature\n4) Read our technicall\u0336y\u0336 white paper (sorry!)\n\nPlease enter the number of your choice (or 'q' to quit): "
            task = input(menu)
        elif white == 2 and task == "4":
            read_white()
            task = input(menu)
    #Farewell message
    print("\nWe hope you enjoyed your time experiencing Natural Intelligence!\nPlease come back soon to discover or suggest new features!\nSee ya!")

def get_suggestion():
    print("Thank you for your willingness to contribute a suggestion! Please enter it below. \nYou have 500 characters and if you provide a valid email address, you will receive an update about your idea.")
    while True:
        sugg = input()
        if len(sugg) < 500:
            break
        else:
            print("That was too long. Try again, more succinctly (max 500 characters).")
    with sqlite3.connect(DB_LOCATION) as con:
        cur = con.cursor()
        #create table if does not exist
        try:
            cur.execute("CREATE TABLE suggestions(suggestion_text)")
        except:
            pass
        #insert suggestion
        cur.execute("INSERT INTO suggestions (suggestion_text) VALUES (?)", ([sugg]))
        con.commit()
    print("Thank you for your suggestion! If you have included a valid email address, you will be notified of its status.")
    return

def read_whitely():
    with open('data/Technically_white_paper.txt', 'r') as f:
        contents = f.read()
        pager(contents)
    return

def read_white():
    console = Console()
    with open('data/Technical_white_paper.md') as f:
        renderable_markup = Markdown(f.read())
        with console.pager():
            console.print(renderable_markup)
    return

if __name__ == "__main__":
    main()
