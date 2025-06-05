from bottle import default_app, route, run, template, request, response, view, redirect
import wikipedia
import sqlite3
import os
from haiku import check_nsyl
#to link db file location with python script location
path = os.path.dirname(os.path.realpath(__file__))
DB_LOCATION = os.path.join(path, "nini.db")

@route('/')
@view('menu')
def main():
    try:
        feat = request.get_cookie("feat")
    except:
        feat = None
    try:
        white = request.get_cookie("white")
    except:
        white = None
    return dict(feat=feat, white=white)

@route('/whitepaper')
def white_paper():
    response.set_cookie("white", "yes")
    return template("white")

@route('/paperwhite')
def paper_white():
    return template("paper")

@route('/search')
def search_w():
    return template("search")

@route('/search', method='POST')
@view('search_result')
def get_result():
    response.set_cookie("feat", "yes")
    res = []
    wikipedia.set_lang("en")
    searx = request.forms.searx
    try:
        results = wikipedia.search(searx, 1, suggestion=False)
        for result in results:
            try:
                page = wikipedia.WikipediaPage(result)
                url = page.url
                summary = page.summary
                res.append((result, url, summary))
            except wikipedia.exceptions.DisambiguationError as e:
                options = e.options[:3]
                for option in options:
                    page = wikipedia.WikipediaPage(option)
                    url = page.url
                    summary = page.summary
                    res.append((option, url, summary))
        return dict(res=res, message=None)
    except wikipedia.exceptions.WikipediaException:
        message = "We could not complete your search due to a temporary problem. Please try again later."
        return dict(message=message, res=None)

@route('/genie/1')
@view('haiku_prompt')
def prompt():
    #Verse 1: place, 5 syllables
    prompt = {1: "Think of a specific place: it could be your favorite place in the world, or the place where you have been the happiest in your life, or another particular place that has a special meaning for you. Please enter below a very short description of this place, or just one part of it.", 2: "Your description needs to have a length of five syllables, when spoken out loud. It is okay to use your fingers to count! Examples of five-syllable descriptions of a place are: 'By a mountain lake', 'Copacabana', 'My mother's garden'.", 3: "Your turn!"}
    step = 1
    return dict(step=step, prompt=prompt, message=None, haiku=None)

@route('/genie/1', method="POST")
@view('haiku_prompt')
def get_verse():
    phrase1 = request.forms.verse_1
    numsyl = 5
    while not check_nsyl(phrase1, numsyl):
        message = "This does not seem to have the correct number of syllables. Try again!"
        prompt = {1: "Think of a specific place: it could be your favorite place in the world, or the place where you have been the happiest in your life, or another particular place that has a special meaning for you. Please enter below a very short description of this place, or just one part of it.", 2: "Your description needs to have a length of five syllables, when spoken out loud. It is okay to use your fingers to count! Examples of five-syllable descriptions of a place are: 'By a mountain lake', 'Copacabana', 'My mother's garden'.", 3: "Your turn!"}
        step = 1
        return dict(step=step, prompt=prompt, message=message, haiku=None)
    haiku = ''
    haiku += phrase1 + "\n"
    step = 2
    message = "Well done."
    prompt = {1: "Now, imagine yourself in this place, which you know so well. Look around, visualize all the details. Remember what makes this place special for you, specifically. Then, please describe a change: any type of change, anything that happens, or has happened, to this place, or at this place, to you, to someone else, to no one at all.", 2: "This time, you have seven syllables! Examples of a seven-syllable description of a change are: 'Dark grey clouds fill up the sky', 'The waitress folds her apron', 'Overgrown weeds everywhere'.", 3: "Your turn!"}
    return dict(step=step, prompt=prompt, message=message, haiku=haiku)

@route('/genie/2', method="POST")
@view('haiku_prompt')
def get_verse_2():
    phrase2 = request.forms.verse_2
    haiku = request.forms.haiku
    numsyl = 7
    while not check_nsyl(phrase2, numsyl):
        message = "This does not seem to have the correct number of syllables. Try again!"
        prompt = {1: "Imagine yourself in this place, which you know so well. Look around, visualize all the details. Remember what makes this place special for you, specifically. Then, please describe a change: any type of change, anything that happens, or has happened, to this place, or at this place, to you, to someone else, to no one at all.", 2: "This time, you have seven syllables! Examples of a seven-syllable description of a change are: 'Dark grey clouds fill up the sky', 'The waitress folds her apron', 'Overgrown weeds everywhere'.", 3: "Your turn!"}
        step = 2
        return dict(step=step, prompt=prompt, message=message)
    haiku += phrase2 + "\n"
    step = 3
    message = "Well done."
    prompt = {1: "Finally, having visualized this special place, and described a change that happens or happened in relation to it, imagine how someone might have felt, witnessing that change, while being in that place. Describe a feeling, a thought, a sensation, which come as a response to that change.", 2: "You only have five syllables! Examples of a five-syllable description of a feeling, sensation, or thought, are: 'Suddenly I\'m cold', 'Another cocktail?', 'How tired one gets'.", 3: "Your turn !"}
    return dict(step=step, prompt=prompt, message=message, haiku=haiku)

@route('/genie/3', method="POST")
@view('haiku_prompt')
def get_verse_3():
    phrase3 = request.forms.verse_3
    haiku = request.forms.haiku
    numsyl = 5
    while not check_nsyl(phrase3, numsyl):
        message = "This does not seem to have the correct number of syllables. Try again!"
        prompt = {1: "Finally, having visualized this special place, and described a change that happens or happened in relation to it, imagine how someone might have felt, witnessing that change, while being in that place. Describe a feeling, a thought, a sensation, which come as a response to that change.", 2: "You only have five syllables! Examples of a five-syllable description of a feeling, sensation, or thought, are: 'Suddenly I\'m cold', 'Another cocktail?', 'How tired one gets'.", 3: "Your turn !"}
        step = 3
        return dict(step=step, prompt=prompt, message=message)
    haiku += phrase3
    with sqlite3.connect(DB_LOCATION) as con:
        cur = con.cursor()
        #create table if not exist
        cur.execute("CREATE TABLE IF NOT EXISTS haiku(haiku_text)")
        #insert haiku
        cur.execute("INSERT INTO haiku (haiku_text) VALUES (?)", [haiku])
        con.commit()
    return redirect('/genie/result')


@route('/genie/result')
def return_haiku():
    response.set_cookie("feat", "yes")
    with sqlite3.connect(DB_LOCATION) as con:
        cur = con.cursor()
        cur.execute("SELECT * FROM haiku")
        haikus = cur.fetchall()
    haiku = haikus[-1]
    return template("haiku_read", haiku=haiku)

@route('/genie/anthology', method="POST")
@view('anthology')
def anthology_optin():
    haiku = request.forms.haiku
    author = request.forms.author
    date = request.forms.date
    with sqlite3.connect(DB_LOCATION) as con:
        cur = con.cursor()
        #create table if not exist
        cur.execute("CREATE TABLE IF NOT EXISTS anthology(haiku, author, date)")
        #insert haiku
        cur.execute("INSERT INTO anthology (haiku, author, date) VALUES (?, ?, ?)", (haiku, author, date))
        con.commit()
        cur.execute("SELECT * FROM anthology")
        anthology = cur.fetchall()
        return dict(anthology=anthology)

'''@route('/genie/anthology')
@view('anthology')
def anthology_view():
    with sqlite3.connect(DB_LOCATION) as con:
        cur = con.cursor()
        cur.execute("SELECT * FROM anthology")
        anthology = cur.fetchall()
        return dict(anthology=anthology)
        '''

@route('/suggest')
def get_suggestion():
    return template("suggest", message=None)

@route('/suggest', method='POST')
@view('suggest')
def record_suggestion():
    response.set_cookie("feat", "yes")
    suggestion = request.forms.suggestion
    email = request.forms.email
    with sqlite3.connect(DB_LOCATION) as con:
        cur = con.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS suggestions(suggestion_text, email)")
        #insert suggestion
        cur.execute("INSERT INTO suggestions (suggestion_text, email) VALUES (?, ?)", (suggestion, email))
        con.commit()
    message = "Thank you for your suggestion! If you have included a valid email address, you will be notified of its status."
    return dict(message=message)

application = default_app()

if __name__ == "__main__":
    run(host='localhost', port=8080, debug=True)


