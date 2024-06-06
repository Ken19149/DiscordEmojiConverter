import pyperclip
output = ""
while True:
    text = input()
    for i in text:
        if i.lower() in "abcdefghijklmnopqrstuvwxyz":
            output = output + (":regional_indicator_" + i + ": ")
        elif i in "0123456789":
            output = output + (":number_" + i + ": ")
        elif i in "?!":
            output = output + (i.replace("?", " :question: ").replace("!", " :exclamation: "))
        elif i == " ":
            output = output + (i.replace(" ", "\n"))
        else:
            continue
    pyperclip.copy(output)
    print(output)
    output = ""