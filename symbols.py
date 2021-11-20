import PySimpleGUI as sg
import xerox 

ALL_SYMBOLS = []
with open('./symbols.txt') as fil:
    for line in fil:
        line = line.replace(f" ", f"")
        line = line.replace("\n", "")

        symbols = line.split(',')
        ALL_SYMBOLS.append(symbols)


layout = []
for SYMBOL_LIST in ALL_SYMBOLS:
    button_list = []
    print(SYMBOL_LIST)
    for symbol in SYMBOL_LIST:
        button_list.append(sg.Button(symbol, size=(1,1)))
    layout.append(button_list)

sg.theme('black')
window = sg.Window('AutoComplete', layout, return_keyboard_events=True, finalize=True, font= ('Helvetica', 16))

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    
    if event != sg.WIN_CLOSED:
        xerox.copy(event)
window.close()