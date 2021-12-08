import random
import os
import time

def onpromo():
    print(f"{igen}                                                                                                                                                          by SzBalesz\033[97m")

#színek változtatása
szin = "\033[91m"
kockaszin = "\033[97m"
szamszin = "\033[93m"
emoji = "🎲"
igen = "\033[1;90m"

#kockák :)
os.system("cls")
def kocka(y):
    if y == 1:
        print(f"""
{szin}┌─────────━▒ {emoji} ▒━────────┐{kockaszin}

         .-------.
         |       |
         |   o   |
         |       |
         '-------'

{szin}└─────────━▒{szamszin} {szam} {szin}▒━─────────┘
        """)
    elif y == 2:
        print(f"""
{szin}┌─────────━▒ {emoji} ▒━────────┐{kockaszin}

         .-------.
         |  o    |
         |       |
         |    o  |
         '-------'

{szin}└─────────━▒{szamszin} {szam} {szin}▒━─────────┘
        """)
    if y == 3:
        print(f"""
{szin}┌─────────━▒ {emoji} ▒━────────┐{kockaszin}

         .-------.
         | o     |
         |   o   |
         |     o |
         '-------'

{szin}└─────────━▒{szamszin} {szam} {szin}▒━─────────┘
        """)
    elif y == 4:
        print(f"""
{szin}┌─────────━▒ {emoji} ▒━────────┐{kockaszin}

         .-------.
         | o   o |
         |       |
         | o   o |
         '-------'

{szin}└─────────━▒{szamszin} {szam} {szin}▒━─────────┘
        """)
    if y == 5:
        print(f"""
{szin}┌─────────━▒ {emoji} ▒━────────┐{kockaszin}

         .-------.
         | o   o |
         |   o   |
         | o   o |
         '-------'

{szin}└─────────━▒{szamszin} {szam} {szin}▒━─────────┘
        """)
    elif y == 6:
        print(f"""
{szin}┌─────────━▒ {emoji} ▒━────────┐{kockaszin}

         .-------.
         | o o o |
         |       |
         | o o o |
         '-------'

{szin}└─────────━▒{szamszin} {szam} {szin}▒━─────────┘
        """)

#dobás folyamata
for x in range(30, 1, -1):
    szam = random.randint(1, 6)
    onpromo()
    kocka(szam)
    time.sleep(1/(x+1))
    os.system("cls")
#önpromó xd
igen = "\033[1;91m"
onpromo()
#kipörgetett kocka kiiratása
kockaszin = "\033[1;32m"
kocka(szam)
