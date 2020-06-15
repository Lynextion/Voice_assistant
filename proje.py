from gtts import gTTS
import speech_recognition as sr
import playsound
import time
from acti import activity
from youtu import youtube
from yt import download 
from sansür_ekleme import delete
from bs2 import amazon



         

def listen():





    with sr.Microphone() as source:

        r = sr.Recognizer()
        r.adjust_for_ambient_noise(source)
        print("sendeyiz")
        audio = r.listen(source)

        data = ""

        try:
            data = r.recognize_google(audio,language = "tr-tr")
            data= data.lower()
            print("şunu dedin "+data)

        except sr.UnknownValueError:
            print("ağa anlamadım")
            
        


        return data

def komut(data):
    data = data.split()


    if "sıkıldı" in data:
        activity()
        
    if "youtube" in data:
        youtube(data)

    if "indir" in data:
         download()

    if "sil" in data:
        delete()
    if "amazon"in data:
        amazon(data)


def play(data):
    tts = gTTS(text=str(data),lang="tr")
    tts.save("merhaba.mp3")
    playsound.playsound('merhaba.mp3', True)


data = ''   

wait = 0


while(data != 'çıkış'):

    data = listen()

    if data.split() == 'bekle':
        wait = 1

    if data.split() == "devam":
        wait = 0


    if wait !=  1:
        komut(data)
    play(data)