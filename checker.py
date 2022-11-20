import sys
import re

from moneywagon import AddressBalance
from time import sleep
from urllib.request import urlopen

def wrongwallet():
    print("Wallet address is wrong.")
    exit(1)

def slowsrc(addr):
    global balanceout
    total = AddressBalance().action('btc', addr)
    balanceout= str(total)

def fastsrc(addr):
    global balanceout
    satoshis = 1e+8
    htmlfile = urlopen("https://blockchain.info/address/%s?format=json" % addr, timeout = 10)
    htmltext = htmlfile.read().decode('utf-8')
    btc_tokens = float( re.search( r'%s":(\d+),' % 'final_balance', htmltext ).group(1) )
    balanceout = str(btc_tokens/satoshis)

def main():
    print("\n-----------------------------------------------------------aa")
    print("            albertopisaroni/btc-balance-checker")
    print("-----------------------------------------------------------\n")
    addr = input("Enter a BTC Address :>  ")
    try:
        try:
            fastsrc(addr)
        except:
            slowsrc(addr)
    except:
        wrongwallet()
    if ("None" in balanceout):
        wrongwallet()
    print("     You have found :>  " + balanceout + " BTC")

if __name__ == '__main__':
    main()
