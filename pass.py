import PySimpleGUI as sg
import string
import random

layout = [
[sg.Text('Uppercase:',size=(15,1)),sg.InputText(key='-UPPER-')],
[sg.Text('Lowercase:',size=(15,1)),sg.InputText(key='-LOWER-')],
[sg.Text('Digits:',size=(15,1)),sg.InputText(key='-DIGITS-')],
[sg.Text('Symbols:',size=(15,1)),sg.InputText(key='-SYMBOLS-')],
[sg.Button('Ok', key='-OK-'),sg.Button('Cancel',key='-CANCEL-')],
[sg.Text('Password'),sg.InputText(key='-OUTPUT-')]
]

def generate_password(upper, lower, digits, symbols):
    password=[]
    for i in range(upper):
        upper = random.choice(string.ascii_uppercase)
        password.append(upper)
    for i in range(lower):
        lower = random.choice(string.ascii_lowercase)
        password.append(lower)
    for i in range(digits):
        digits = random.choice(string.digits)
        password.append(digits)
    for i in range(symbols):
        symbols = random.choice(string.punctuation)
        password.append(symbols)
    random.shuffle(password)
    final = ''.join(password)
    return final
    
    


window = sg.Window('Password Generator',layout)
while True:
    event,values = window.read()
    if event in (sg.WIN_CLOSED or '-CANCEL-'):
        break
    if event == '-OK-':
        upper = int(values['-UPPER-'])
        lower = int(values['-LOWER-'])
        digits = int(values['-DIGITS-'])
        symbols = int(values['-SYMBOLS-'])
        final = generate_password(upper,lower,digits,symbols)
        window['-OUTPUT-'].update(final)

window.close()
