import random
import string
print("Password Generator...")
length=int(input("Enter Password length..."))
use_upper=input("Include uppercase(y/n):").lower()
use_lower=input("Include lowercase(y/n):").lower()
use_digits=input("Include digits(y/n):").lower()
use_symbol=input("Include symbol(y/n):").lower()
uppercase=string.ascii_uppercase
lowercase=string.ascii_lowercase
digits=string.digits
symbols="!@#$%^&*"
pool=lowercase
if use_upper=='y':
    pool+=uppercase
if use_digits=='y':
    pool+=digits
if use_symbol=='y':
    pool+=symbols
password=""
for i in range(length):
    password+=random.choice(pool)
print("Your final password is here...")
print("!PASSWORD!:",password)    


