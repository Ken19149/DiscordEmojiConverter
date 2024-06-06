import pyperclip

pair = [["?", "question"], ["!", "exclamation"]]

output = ""
while True:
    text = input()
    for i in text:
        if "a" <= i.lower() <= "z": # alphabet
            output = output + (":regional_indicator_" + i.lower() + ": ")
        elif "0" <= i <= "9":       # number
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