from modules.assistant import greet, listen
from modules.web_handler import search_wikipedia, open_website
from modules.email_handler import send_email
from modules.music_handler import stream_music
from modules.ott_handler import open_ott
from modules.calendar_handler import add_event_to_calendar
import re

def main():
    greet()
    while True:
        command = listen()

        if "time" in command:
            from datetime import datetime
            current_time = datetime.now().strftime("%I:%M %p")
            print(f"The current time is {current_time}")

        elif "wikipedia" in command:
            search_wikipedia(command)

        elif "open youtube" in command:
            open_website("https://www.youtube.com")

        elif "send email" in command:
            send_email()

        elif "play music" in command:
            stream_music()

        elif "open netflix" in command:
            open_ott("netflix")

        elif "add event" in command:
            add_event_to_calendar()

        elif re.search(r"(exit|bye|stop|quit)", command):
            print("Goodbye! Have a great day.")
            break

        else:
            print("Sorry, I don't understand that command. Can you please repeat?")

if __name__ == "__main__":
    main()
