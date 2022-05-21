import re

# чистим строчку
def clean(string):
    s = repr(string)
    badwords = ['<|startoftext|>', '<|endoftext|>']
    for i in badwords:
        s = s.replace(i, '')
    s = re.sub(r"\\xa0", " ", s)
    s = re.sub(r"[@#$%^&*{}\\\"\[\]\|`'Х/<>a-zA-Z]", "", s)
    s = re.sub(" +", " ", s).strip()
    return s

# проверка на наличие неведомых символов
def check(string):

    alph = []
    a = ord('а')
    A = ord('А')
    alph += [chr(i) for i in range(a, a + 32)]
    alph += [chr(i) for i in range(A, A + 32)]
    alph += [str(i) for i in range(0, 10)]
    alph += [' ', '-', '.', ',', ':', ';', '!', '?', '«', '»']

    for i in range(0, len(string)):
        if string[i] not in alph:
            return 0
    return 1

file = open("tagged.txt", "r")
raw_lines = file.readlines()
lines = []

for line in raw_lines:
    s = clean(line)
    if check(s):
        lines.append(s)

with open('cleaned_tagged.txt', 'w') as f:
    for i in lines:
        f.write("%s\n" % i)