import pyperclip
output = ""
while True:
    text = input()
    for i in text:
        if i.lower() in "abcdefghijklmnopqrstuvwxyz":
            output = output + (" :regional_indicator_" + i + ": ")
        elif i in "0123456789":
            output = output + (i.replace("1"," :one: ").replace("2"," :two: ").replace("3"," :three: ").replace("4"," :four: ").replace("5"," :five: ").replace("6"," :six: ").replace("7"," :seven: ").replace("8"," :eight: ").replace("9"," :nine: ").replace("0"," :zero: "))
        elif i == " ":
            output = output + (i.replace(" ", "  "))
        else:
            continue
    pyperclip.copy(output)
    print(output)
    output = ""