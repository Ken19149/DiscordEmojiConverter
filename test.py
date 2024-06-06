import numpy as np

pair = np.array([["?", "question"], ["!", "exclamation"], ["/","slash"]])

out = ""

text = input()

print(pair[:, 0])


for i in text:
    if i in pair[:, 0]:
        out += pair[i][1]
    else:
        out += i

print(out)
