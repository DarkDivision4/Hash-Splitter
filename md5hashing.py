
from selenium import webdriver
import time

url = 'https://md5hashing.net/hash/'
hashlist = open('hashes.txt')
hashes = hashlist.readlines()
hash = []
browser = webdriver.Chrome()

md5 = 'md5'
sha1 = 'sha1'
sha224 = 'sha224'
sha256 = 'sha256'
sha512 = 'sha512'

for i in hashes:
    if len(i) == 33:
        hash.append([i])
        browser.get(url + md5 + '/' + str(hash))
        time.sleep(15)
        if '4 days of fishing' in browser.page_source:
            print('[!] Hash: ' + i, end='')
            print('[!] Algorithm: ' + md5.upper())
            print('[-] Decryption Failed\n')
        else:
            hash_type = browser.find_element_by_xpath('/html/body/div/div/div[1]/main/div[4]/div[1]/div/div[1]/h4/b')
            decoded_hash = browser.find_element_by_xpath('//*[@id="decodedValue"]')
            print('[!] Hash: ' + i, end='')
            print('[!] Algorithm: ' + md5.upper())
            print('[+] Decryption Successful: ' + str(decoded_hash.text) + '\n')
    if len(i) == 41:
        browser.get(url + sha1 + '/' + i)
        time.sleep(15)
        if '4 days of fishing' in browser.page_source:
            print('[!] Hash: ' + i, end='')
            print('[!] Algorithm: ' + sha1.upper())
            print('[-] Decryption Failed\n')
        else:
            hash_type = browser.find_element_by_xpath('/html/body/div/div/div[1]/main/div[4]/div[1]/div/div[1]/h4/b')
            decoded_hash = browser.find_element_by_xpath('//*[@id="decodedValue"]')
            print('[!] Hash: ' + i, end='')
            print('[!] Algorithm: ' + sha1.upper())
            print('[+] Decryption Successful: ' + str(decoded_hash.text) + '\n')
    if len(i) == 57:
        browser.get(url + sha224 + '/' + i)
        time.sleep(15)
        if '4 days of fishing' in browser.page_source:
            print('[!] Hash: ' + i, end='')
            print('[!] Algorithm: ' + sha224.upper())
            print('[-] Decryption Failed\n')
        else:
            hash_type = browser.find_element_by_xpath('/html/body/div/div/div[1]/main/div[4]/div[1]/div/div[1]/h4/b')
            decoded_hash = browser.find_element_by_xpath('//*[@id="decodedValue"]')
            print('[!] Hash: ' + i, end='')
            print('[!] Algorithm: ' + sha224.upper())
            print('[+] Decryption Successful: ' + str(decoded_hash.text) + '\n')
    if len(i) == 65:
        browser.get(url + sha256 + '/' + i)
        time.sleep(15)
        if '4 days of fishing' in browser.page_source:
            print('[!] Hash: ' + i, end='')
            print('[!] Algorithm: ' + sha256.upper())
            print('[-] Decryption Failed\n')
        else:
            hash_type = browser.find_element_by_xpath('/html/body/div/div/div[1]/main/div[4]/div[1]/div/div[1]/h4/b')
            decoded_hash = browser.find_element_by_xpath('//*[@id="decodedValue"]')
            print('[!] Hash: ' + i, end='')
            print('[!] Algorithm: ' + sha256.upper())
            print('[+] Decryption Successful: ' + str(decoded_hash.text) + '\n')
    if len(i) == 97:
        browser.get(url + sha384 + '/' + i)
        time.sleep(15)
        if '4 days of fishing' in browser.page_source:
            print('[!] Hash: ' + i, end='')
            print('[!] Algorithm: ' + sha384.upper())
            print('[-] Decryption Failed\n')
        else:
            hash_type = browser.find_element_by_xpath('/html/body/div/div/div[1]/main/div[4]/div[1]/div/div[1]/h4/b')
            decoded_hash = browser.find_element_by_xpath('//*[@id="decodedValue"]')
            print('[!] Hash: ' + i, end='')
            print('[!] Algorithm: ' + sha384.upper())
            print('[+] Decryption Successful: ' + str(decoded_hash.text) + '\n')
    if len(i) == 129:
        browser.get(url + sha512 + '/' + i)
        time.sleep(15)
        if '4 days of fishing' in browser.page_source:
            print('[!] Hash: ' + i, end='')
            print('[!] Algorithm: ' + sha512.upper())
            print('[-] Decryption Failed\n')
        else:
            hash_type = browser.find_element_by_xpath('/html/body/div/div/div[1]/main/div[4]/div[1]/div/div[1]/h4/b')
            decoded_hash = browser.find_element_by_xpath('//*[@id="decodedValue"]')
            print('[!] Hash: ' + i, end='')
            print('[!] Algorithm: ' + sha512.upper())
            print('[+] Decryption Successful: ' + str(decoded_hash.text) + '\n')
browser.close()
