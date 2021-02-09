# Author: Dark Division
# Function: Hash Cracker

import requests
from auth import *

url = 'http://md5decrypt.net/Api/api.php?hash='
hash = []
wordlist = open('hashes.txt')
cracked_hashes = open('cracked.txt', 'a')
hash_list = wordlist.readlines()

for i in hash_type:
    for x in hash_list:
        hash.append([x])
        r = requests.get('https://md5decrypt.net/Api/api.php?hash=' + str(hash).strip("'\/n'[]") + '&hash_type=' + i + '&email=' + user + '&code=' + key)
        hash.remove([x])
        
        if x.isupper() == True:
            if i == 'md5':
                continue
        if x.islower() == True:
            if i == 'ntlm':
                continue
        if len(r.text) == 0:
            print('[!] Hash: ' + x, end='')
            print('[!] Algorithm: ' + i.upper())
            print('[-] Decryption: Failed\n')

        if 'CODE ERREUR' not in str(r.text) and len(r.text) != 0:
            print('[!] Hash: ' + x, end='')
            print('[!] Algorithm: ' + i.upper())
            print('[+] Hash Decrypted: ' + r.text + '\n')
            cracked_hashes.write('Hash:' + x + 'Decrypted Hash:' + r.text + '\r')
        
