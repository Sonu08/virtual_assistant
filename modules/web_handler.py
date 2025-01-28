import webbrowser
import wikipedia

def open_website(url):
    webbrowser.open(url)
    print(f"Opening {url}")

def search_wikipedia(query):
    try:
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        print(f"According to Wikipedia: {results}")
    except Exception as e:
        print("Sorry, I couldn't find any information on that.")
