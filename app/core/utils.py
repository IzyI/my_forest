import time
import uuid
import hashlib
from datetime import datetime


def check_token(token, word):
    password, salt = token.split('w0w6cdeda2w8')
    word = word + datetime.today().strftime("%d/%m/%y_%H:%M")
    return password == hashlib.sha512(salt.encode() + word.encode()).hexdigest()

def create_token(word):
    salt = uuid.uuid4()
    salt = salt.hex
    word = word + datetime.today().strftime("%d/%m/%y_%H:%M")
    return hashlib.sha512(salt.encode() + word.encode()).hexdigest() + 'w0w6cdeda2w8' + salt





if __name__ == "__main__":
    a=input()
    a = create_token(a)
    print(f"create_token {a}")
    a = check_token(a, "qwerty")
