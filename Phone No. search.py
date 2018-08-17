''' This program searches for indian phone numbers starting with country code"+91"
    and the phone number must be 13 digits long.
    The special thing about this program is that it will search from anything that
    is copied to the clipboard, be it a website column , long paragraphs etc.. '''

import pyperclip

def isphone2(text):
    if len(text) != 11:
        return False
    for i in range(0,11):
        if not text[i].isdecimal():
            return False
    return True


def isphone(text):
    if len(text) != 13:
        return False
    if text[0] != "+":
        return False
    for i in range(1,13):
        if not text[i].isdecimal:
            return False
    return True

message=pyperclip.paste()

foundnumber=False

for i in range(len(message)):
    chunk=message[i:i+13]
    if isphone(chunk):
        print("Phone Number found : " + chunk)
        foundnumber=True
    chunk=message[i:i+11]
    if isphone2(chunk):
        print("Phone Number found : " + chunk)


if not foundnumber:
    print("Couldn't find any number")