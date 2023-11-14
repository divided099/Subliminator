import os
try:
    from io import BytesIO
    from colorama import Fore, Style
    import webbrowser
    import platform
    import pygame
    import requests
except:
    os.system("pip install -r requirements.txt")

audio_url = "https://cdn.discordapp.com/attachments/1155459150747271250/1156591694721060925/PEl6PTw.mp3?ex=65158774&is=651435f4&hm=68c67fbf639008db809c1e86e2e12af4debef3c852d31620c923bb99544054e3"
response = requests.get(audio_url)
audio_data = BytesIO(response.content)
pygame.mixer.init()
pygame.mixer.music.load(audio_data)
pygame.mixer.music.play()

def clear():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

clear()
banner = '''
  _________    ___.   .__  .__        .__               __                
 /   _____/__ _\_ |__ |  | |__| _____ |__| ____ _____ _/  |_  ___________ 
 \_____  \|  |  \ __ \|  | |  |/     \|  |/    \\__  \\   __\/  _ \_  __ \
 /        \  |  / \_\ \  |_|  |  Y Y  \  |   |  \/ __ \|  | (  <_> )  | \/
/_______  /____/|___  /____/__|__|_|  /__|___|  (____  /__|  \____/|__|   
        \/          \/              \/        \/     \/                  
                            discord.gg/my7hW7aSSQ
'''

print(Fore.BLUE)
menu = '''
[1] Subliminal Lookup
[2] Downloadable
[3] Voices
[4] Sound Effects
[5] Mix with Kinemaster
'''

def subliminal_lookup():
    sbl = input("\t\t\tLookup Subliminal Message: ")
    webbrowser.open_new_tab(f"https://www.youtube.com/results?search_query={sbl}")

def downloadable():
    webbrowser.open_new_tab("https://example.com")

def voices():
    webbrowser.open_new_tab("https://www.google.com/search?q=ai+voices+online&oq=ai+voices+online&aqs=chrome..69i57.3028j0j4&sourceid=chrome&ie=UTF-8")

def sound_effects():
    webbrowser.open_new_tab("https://www.zapsplat.com/sound-effect-categories/")

def mix_wk():
    pass
    #wtf how will this even work 💀

while True:
    clear()
    print(f"\t\t\t\t{banner}\n")
    print(f"\t\t\t{menu}")
    user = input("Command: ")
    if user == "exit":
        clear()
        exit()
    elif user == "1":
        subliminal_lookup()
    elif user == "2":
        downloadable()
    elif user == "3":
        voices()
    elif user == "4":
        sound_effects()
    elif user == "5":
        mix_wk()