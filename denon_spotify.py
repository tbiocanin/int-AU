import os 
import sys
import json
import spotipy
import webbrowser
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials
from json.decoder import JSONDecodeError
from datetime import datetime
import time

CLIENT_ID = ''
CLIENT_SECRET = ''
REDIRECT_URI = 'https://google.com/'
scope = 'user-read-private user-read-playback-state user-modify-playback-state'

#get the username from terminal
username = sys.argv[1]

#rhylvu2oo8mcm2so03afyz8hv ID mog naloga
#mojID = 'rhylvu2oo8mcm2so03afyz8hv'

#brisi kes i pitaj korisnika da li moze da radi svaki put kada 
#pokrene novi program
try:
    token = util.prompt_for_user_token(username, scope, client_id=CLIENT_ID, client_secret=CLIENT_SECRET, redirect_uri=REDIRECT_URI)
except (AttributeError, JSONDecodeError):
    os.remove(f".cache-{username}")
    token = util.prompt_for_user_token(username, scope, client_id=CLIENT_ID, client_secret=CLIENT_SECRET, redirect_uri=REDIRECT_URI)

#spotify object
sp = spotipy.Spotify(auth=token)

# links to the devices that are opta
uredjaj_telefon = ''
uredjaj_komp = ''
uredjaj_denon = ''

# links to the playlist 
eurobeat = ''
#nocna muzika
klasika = ''
#next_track(device_id=None)
#time.sleep(3) spavaj tri sekunde

def morning_mode():
    sp.start_playback(device_id=uredjaj_denon, context_uri=eurobeat)
    print("dobro jutro")

def night_mode():
    sp.start_playback(device_id=uredjaj_denon, context_uri=klasika)
    print("laku noc")

def dnevnjak():
    sp.start_playback(device_id=uredjaj_denon, context_uri=eurobeat)
    sp.shuffle(state = True, device_id=uredjaj_denon)
    time.sleep(45)
    sp.next_track(device_id=uredjaj_denon)
#simple alarm clock that will work over the terminal


def validate_time(alarm_time):
    if len(alarm_time) != 11:
        return "Los format, pokusaj ponovo!"
    else:
        if int(alarm_time[0:2]) > 12:
            return "Los format sati, pokusaj ponovo!"
        elif int(alarm_time[3:5]) > 59:
            return "Los format minuta, pokusaj ponovo!"
        elif int(alarm_time[6:8]) > 59:
            return "Los format sekundi, pokusaj ponovo!"
        else:
            return "ok"

while True:
    alarm_time = input("Uneti vreme u 'HH:MM:SS AM/PM' formatu: ")
    
    validate = validate_time(alarm_time.lower())
    if validate != "ok":
        print(validate)
    else:
        print(f"Setting alarm for {alarm_time}...")
        break

alarm_hour = alarm_time[0:2]
alarm_min = alarm_time[3:5]
alarm_sec = alarm_time[6:8]
alarm_period = alarm_time[9:].upper()

while True:
    now = datetime.now()

    current_hour = now.strftime("%I")
    current_min = now.strftime("%M")
    current_sec = now.strftime("%S")
    current_period = now.strftime("%p")

    if alarm_period == current_period:
        if alarm_hour == current_hour:
            if alarm_min == current_min:
                if alarm_sec == current_sec:
                    dnevnjak()
                    print("ZVONIM!")
                    break



