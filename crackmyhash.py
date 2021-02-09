
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

url = 'http://online.crackmyhash.com/'
hashes = open('hashes.txt')
hash_list = hashes.readlines()
all_hashes = []
browser = webdriver.Chrome()

for i in hash_list:
    browser.get(url)
    all_hashes.append([i])
    hash = browser.find_element_by_id('hash')
    code = browser.find_element_by_id('CaptchaDiv')
    code_input = browser.find_element_by_id('CaptchaInput')

    hash.send_keys(i)
    code_input.send_keys(code.text)
    browser.find_element_by_name('button').click()
    time.sleep(4)
    response = browser.find_element_by_class_name('custom_h4')
    if 'Password Not Found' in response.text:
        if len(i) == 33:
            print('[!] Hash: ' + i, end='') 
            print('[!] Algorithm: MD5')
            print('[-] Decryption Failed\n')
        elif len(i) == 41:
           print('[!] Hash: ' + i, end='') 
           print('[!] Algorithm: SHA1')
           print('[-] Decryption Failed\n')
        elif len(i) == 65:
           print('[!] Hash: ' + i, end='') 
           print('[!] Algorithm: SHA256')
           print('[-] Decryption Failed\n')
        elif len(i) == 129:
           print('[!] Hash: ' + i, end='') 
           print('[!] Algorithm: SHA512')
           print('[-] Decryption Failed\n')
    else:
        if len(i) == 33:
           print('[!] Hash: ' + i, end='') 
           print('[!] Algorithm: MD5')
           print('[-] Decryption Successful: ' + response.text + '\n')
        elif len(i) == 41:
           print('[!] Hash: ' + i, end='') 
           print('[!] Algorithm: SHA1')
           print('[-] Decryption Successful: ' + response.text + '\n')
        elif len(i) == 65:
           print('[!] Hash: ' + i, end='') 
           print('[!] Algorithm: SHA256')
           print('[-] Decryption Successful: ' + response.text + '\n')
        elif len(i) == 129:
           print('[!] Hash: ' + i, end='') 
           print('[!] Algorithm: SHA512')
           print('[-] Decryption Successful: ' + response.text + '\n')
    all_hashes.remove([i])
browser.close()
