import random
import os
import time

def onpromo():
    print(f"{igen}                                                                                                                                                          by SzBalesz\033[97m")

#szΓ­nek vΓ‘ltoztatΓ‘sa
szin = "\033[91m"
kockaszin = "\033[97m"
szamszin = "\033[93m"
emoji = "π²"
igen = "\033[1;90m"

#kockΓ‘k :)
os.system("cls")
def kocka(y):
    if y == 1:
        print(f"""
{szin}ββββββββββββ {emoji} βββββββββββ{kockaszin}

         .-------.
         |       |
         |   o   |
         |       |
         '-------'

{szin}ββββββββββββ{szamszin} {szam} {szin}ββββββββββββ
        """)
    elif y == 2:
        print(f"""
{szin}ββββββββββββ {emoji} βββββββββββ{kockaszin}

         .-------.
         |  o    |
         |       |
         |    o  |
         '-------'

{szin}ββββββββββββ{szamszin} {szam} {szin}ββββββββββββ
        """)
    if y == 3:
        print(f"""
{szin}ββββββββββββ {emoji} βββββββββββ{kockaszin}

         .-------.
         | o     |
         |   o   |
         |     o |
         '-------'

{szin}ββββββββββββ{szamszin} {szam} {szin}ββββββββββββ
        """)
    elif y == 4:
        print(f"""
{szin}ββββββββββββ {emoji} βββββββββββ{kockaszin}

         .-------.
         | o   o |
         |       |
         | o   o |
         '-------'

{szin}ββββββββββββ{szamszin} {szam} {szin}ββββββββββββ
        """)
    if y == 5:
        print(f"""
{szin}ββββββββββββ {emoji} βββββββββββ{kockaszin}

         .-------.
         | o   o |
         |   o   |
         | o   o |
         '-------'

{szin}ββββββββββββ{szamszin} {szam} {szin}ββββββββββββ
        """)
    elif y == 6:
        print(f"""
{szin}ββββββββββββ {emoji} βββββββββββ{kockaszin}

         .-------.
         | o o o |
         |       |
         | o o o |
         '-------'

{szin}ββββββββββββ{szamszin} {szam} {szin}ββββββββββββ
        """)

#dobΓ‘s folyamata
for x in range(30, 1, -1):
    szam = random.randint(1, 6)
    onpromo()
    kocka(szam)
    time.sleep(1/(x+1))
    os.system("cls")
#ΓΆnpromΓ³ xd
igen = "\033[1;91m"
onpromo()
#kipΓΆrgetett kocka kiiratΓ‘sa
kockaszin = "\033[1;32m"
kocka(szam)
