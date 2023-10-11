import locale as loc
from logger import *
import json, re

#These settings are needed:
#logg settings
#language settings
#ad settings
#migrating old settings

def migrate_settings():
    with open("ad setting.txt", "r") as file:
        ad=file.read()
    
    if ad=="true":
        ad=True
    if ad=="false":
        ad=False

    with open("lang.txt", "r") as file:
        language=file.read()

    with open("logg.txt", "r") as file:
        logg=file.read()
    
    if logg=="true":
        logg=True
    if logg=="false":
        logg=False
    
    upcheck=True

    prompt="W.I.P"

    settings={
        "language":language,
        "ad":ad,
        "prompt":prompt,
        "update":upcheck,
        "logging":logg
    }
    with open("settings.json", "w") as save:
        json.dump(settings, save)
    return language, ad, logg, prompt, upcheck

def settings_init():
    get_lang=loc.getdefaultlocale()[:1]
    systemlang=str(get_lang)
    if systemlang.lower()=="('de_de',)":
        language="de"
    if systemlang.lower()=="('en_en',)":
        language="en"
    if systemlang.lower()!="('en_en',)" or systemlang.lower()!="('de_de',)":
        print(f"\nNo compatible language automatically found, Chose English.")
        language="en"
    
    ad=True

    prompt="{name}@{host}:~$ "

    upcheck=True

    logg=True

    settings={
        "language":language,
        "ad":ad,
        "prompt":prompt,
        "update":upcheck,
        "logging":logg
    }

    with open("settings.json", "w") as save:
        json.dump(settings, save)
    return

def change_settings(language, setting):
    with open("settings.json", "r") as file:
        settings=json.load(file)
    
    language=settings.get("language")
    ad=settings.get("ad")
    prompt=settings.get("prompt")
    upcheck=settings.get("update")
    logg=settings.get("logging")
    print(f"{language}\n\n{setting}")


    if setting=="ad":
        if language=="en":
            print("Do you wanna see the ad on every Startup and reboot?")
            answer=input("Yes or No? ")
        
        if language=="de":
            print("Willst du die Werbung sehen wenn fu es startest oder neu startest")
            answer=input("Ja oder Nein? ")

        if answer.lower()=="no" or answer.lower()=="nein":
            ad=False
        if answer.lower()=="yes" or answer.lower()=="ja":
            ad=True

    if setting=="language":
        if language=="en":
            print("There is currently only German and English, What do you choose?")
            answer=input("German or English? ")
        
        if language=="de":
            print("Da ist momentan nur Deutsch und Englisch, was wählst du? ")
            answer=input("Deutsch oder Englisch? ")
        
        if answer.lower()=="german" or answer.lower()=="deutsch":
            language="de"
        if answer.lower()=="english" or answer.lower()=="englisch":
            language="en"
    
    if setting=="prompt":
        prompt=input("What prompt look? ")
    
    if setting=="update":
        if language=="en":
            print("Do youn wanna Check for updates?")
            answer=input("Yes or No? ") 
        
        if language=="de":
            print("Willst du nach updates schauen?")
            answer=input("Ja oder Nein? ").lower()

    if setting=="logging":
        if language=="en":
            print("Should the Stuff be logged? If not, only warnings and errors are gonna be logged.")
            answer=input("Yes or No? ")
            
        if language=="de":
            print("Soll logging angeschalten werden? Wenn nicht, dann werden nur warnungen und fehler geloggt.")
            answer=input("Ja oder Nein? ").lower()
    
    settings={
        "language":language,
        "ad":ad,
        "prompt":prompt,
        "update":upcheck,
        "logging":logg
    }

    with open("settings.json", "w") as file:
        json.dump(settings, file)

    return

def helper(language, logg):
    with open("settings.json", "r") as file:
        settings=json.load(file)
    
    ad=settings.get("ad")
    text="helpsite printed"
    if language == "en":
        print(f"\nThere are the Conversion methods:\n")
        print("The command phex Brings you to the Pseudo Hex converter.")
        print("The command pbin Brings you to the Pseudo Binary converter.")
        print("The connamd legacy pbin Brings you to the Legacy version of the Pseudo Binary converter")
        print("The command hex Brings you to the Hex converter.")
        print("The command bin Brings you to the Binary Converter.")
        print("The command ascii Brings you to the ascii converter.")
        print("The command leetcode brings you to the leetcode converter.")
        print("The command brainfuck Brings you to the Brainfuck converter.")
        print("The command base64 Brings you to the base64 converter.")
        print(f"\nThere are more General commands:\n")
        print("The command ad setting asks if you want to see the ad.")
        print("The command clear screen means that no text from earlier is shown.")
        print("The command Clear Language deletes the file lang.txt")
        print("The command Set Language Creates the lang.txt file and resetting the code to the system language if possible.")
        print("The command reset restarts the program.")
        print("The Command Check Language shows the current language in the lang.txt file.")
        if ad=="true":
            print("The Command Get Game makes the While True: Learn() game stores where you can buy the game.")
        print()
        log_info(text, logg)
                        
    if language == "de":
        print(f"\nDa sind die Converter Methoden:\n")
        print("Der Command phex Bringt dich zum Pseudo Hex converter.")
        print("Der Command pbinary Bringt dich zum Pseudo Binary converter.")
        print("Der Command thex Bringt dich zum Hex converter.")
        print("Der Command tbin Bringt dich zum Binary converter")
        print("Der command ascii Bringt you to the ascii converter.")
        print("Der command leetcode bringt you to the leetcode converter.")
        print("Der command brainfuck Bringt you to the Brainfuck converter.")
        print("Der command base64 Bringt you to the base64 converter.")
        print(f"\nDa sind mehr Generelle Commands:\n")
        print("Der command help Zeigt das hier.")
        print("Der command ad setting fragt ob du die werbung sehen willst.")
        print("Der command clear screen macht das kein text mer von vorhin gezeigt wird.")
        print("Der Command Clear Language Löscht die Datei lang.txt")
        print("Der Command Set Language Macht die Datei lang.txt und startet das Program neu in der Systemsprache wenn möglich.")
        print("Der command reset startet das Program neu.")
        print("Der Commend Check Language zeigt die aktuelle sprache in der lang.txt datei.")
        if ad=="true":
            print("Der Command Get Game zeigt dir was für stores für das Spiel while True: learn() kaufen kann.")
        print()
        log_info(text, logg)
    
    return