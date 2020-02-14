import os
import sys

urls = []
codes = []
keys = []

def add_item(url, code):
    urls.append(url)
    tmp = []
    for i in range(len(url)):
        tmp.append(code[i * 2: i * 2 + 2])
    codes.append(tmp)

def show(url, code):
    print("url:", end='\t')
    for c in url:
        print(c, end='\t')
    print('')

    print("url:", end='\t')
    for c in url:
        print(hex(ord(c)), end='\t')
    print('')

    print("code:", end='\t')
    for i in range(len(url)):
        x = code[i]
        print(' ', x, end='\t')
    print('')

    print("check:", end='\t')
    for i in range(len(url)):
        key = hex(int(code[i], 16) ^ 0xff ^ ord(url[i]))
        if i >= len(keys):
            keys.append(key)
        assert keys[i] == key, "Wrong guess!"
        print(key, end='\t')
    print('')

    print('')

def main(urls, codes):
    n = len(urls)
    print(n)
    for i in range(n):
        show(urls[i], codes[i])

    print('keys:', end='\t')
    for k in keys:
        print(k, end='\t')
    print('')

if __name__ == "__main__":
    with open('code.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            add_item(line.split(' ')[0], line.split(' ')[1])
    main(urls, codes)