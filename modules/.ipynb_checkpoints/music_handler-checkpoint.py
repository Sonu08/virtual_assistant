from pytube import Search
import webbrowser

def stream_music():
    song = input("Enter the song name: ")
    try:
        search = Search(song)
        video = search.results[0]
        webbrowser.open(video.watch_url)
        print(f"Playing: {video.title}")
    except Exception as e:
        print("Sorry, I couldn't find the music.")
