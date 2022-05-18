import time
import colorama
from colorama import Fore
from colorama import Style
import random
import string

print('''
Fake Bitcoin-/Ethereum Miner

Only for educational purpose

Made by Luk-_-btw

Discord: Luk-_-btw#6749
''')

crypto = str(input("Choose between ETH or BTC: "))

if crypto == "ETH" or crypto == "BTC":
    print("Okay. Wallets are being prepared ...")
    time.sleep(3)

    if crypto == "ETH":
        adress = str(input("Please enter your Ethereum adress: "))
    else:
        adress = str(input("Please enter your Bitcoin adress: "))


    class bcolors:
        Won = '\033[92m'
        FAIL = '\033[91m'

        
    def id_gen(size=40, chars=string.ascii_uppercase + string.digits):
        return "".join(random.choice(chars) for _ in range(size))

    tries = 0

    if crypto == "ETH":
        colorama.init()
        while(True):
            if(tries > random.randint(10000000000, 100000000000)):
                print(Fore.GREEN + "[-] 0x" + id_gen() + " | Valid | " + "0.582" + "ETH")
                print("Transfer 0.582 ETH to", adress)
                time.sleep(7)
                tries = 0
                print("Done! Miner is running again!")
                time.sleep(3)
            else:
                print(Fore.RED + "[-] 0x" + id_gen() + " | Invalid | " + "0.00000 ETH")
                tries += 1

    elif crypto == "BTC":
        colorama.init()
        while(True):
            if(tries > random.randint(10000000000, 100000000000)):
                print(Fore.GREEN + "[-] bc1" + id_gen() + " | Valid | " "0.0145" "BTC")
                print("Transfer  0.0145 BTC to", adress)
                time.sleep(7)
                tries = 0
                print("Done! Miner is running again!")
                time.sleep(3)
            else:
                print(Fore.RED + "[-] bc1" + id_gen() + " | Invalid | " + "0.00000 BTC")
                tries += 1
else:
    print("Invalid currency. Please choose betweeen 'ETH' or 'BTC'")