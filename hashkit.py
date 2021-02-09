# Author: Dark Division
# Function: Hash Cracker

import requests
from bs4 import BeautifulSoup

url = 'https://hashtoolkit.com/decrypt-hash/?hash='
user_agent = {'User-agent': 'Mozilla/5.0'}
hashlist = open('hashes.txt')
hashes = hashlist.readlines()

for x in hashes:
    r = requests.get(url + x, headers = user_agent)
    soup = BeautifulSoup(r.text, 'html.parser')
    td = soup.find('td')

    if 'No hashes found' in str(r.text):
        print('[!] Hash: ' + x, end='')
        print('[-] Decryption Failed\n')
    else:
        for i in soup.find_all('span')[10]:
            print('[!] Hash: ' + x, end='')
            print('[!] Algorithm: ' + td.text.upper())
            print('[+] Decryption Successful: ' + i.text + '\n')
