#Made by That-Linux-Programmer aka Nitro Live on GitHub.
import string
import random
import time
#I could not get colorama to work i would like a fellow developer like myself to solve this problem.
print("If you want this to work put it in an IDE instead of this. And then remove the \"break\" command")
print()
time.sleep(2)
print()
bit = 0.00
while True:
    lowercase = string.ascii_lowercase + string.digits
    print("0x" + ''.join(random.choice(lowercase) for i in range(40)) ,"(",bit,"B)")
    digit = random.randint(0, 99999) # Add an extra 9 or other number to make the chance lower.
    if digit ==  2:
        bit = bit + 0.01
        print("0x" + ''.join(random.choice(lowercase) for i in range(40)) ,"(",bit,"B)")
        time.sleep(3)
    elif digit ==  66:
        bit = bit + 0.01
        print("0x" + ''.join(random.choice(lowercase) for i in range(40)) ,"(",bit,"B)")
        time.sleep(3)
    elif digit == 43:
        bit = bit + 0.01
        print("0x" + ''.join(random.choice(lowercase) for i in range(40)) ,"(",bit,"B)")
        time.sleep(3)
    elif digit == 31:
        bit = bit + 0.01
        print("0x" + ''.join(random.choices(lowercase) for i in range(40)) ,"(",bit,"B)")
        time.sleep(3)