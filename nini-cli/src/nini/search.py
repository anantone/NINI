import wikipedia

def main():
    return search_w()

def search_w():
    wikipedia.set_lang("en")
    searx = input("What would you like to learn about?\nType some search keywords or press Enter to move on.\n")
    while searx != "":
        try:
            results = wikipedia.search(searx, 1, suggestion=False)
            for result in results:
                try:
                    page = wikipedia.WikipediaPage(result)
                    url = page.url
                    summary = page.summary
                    print("\n" + result + "\n" + url + "\n" + summary)
                except wikipedia.exceptions.DisambiguationError as e:
                    options = e.options[:2]
                    print("Your search may refer to:\n(if not, try again with more specific search terms)")
                    for option in options:
                        page = wikipedia.WikipediaPage(option)
                        url = page.url
                        summary = page.summary
                        print("\n" + option + "\n" + url + "\n" + summary)
        except wikipedia.exceptions.WikipediaException:
            print("\nWe could not complete your search due to a temporary problem. Please try again later.")
        searx = input("\nYou may try another search below, or press Enter to move on.\n")
    return

if __name__ == "__main__":
    main()
