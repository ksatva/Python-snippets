
#demo
#validateInput.py

while True:
    print('Enter your age: ',end=' ')
    age = input()
    if age.isdecimal():
        break
    print('Pay attention:: enter a number: ',end=' ')

while True:
    print('Select a new password (letters and numbers only): ',end=' ')
    password=input()
    if password.isalnum() and len(password)>=6:
        break
    print('Password must be atleast 6 characters. Only letters and numbers.')
