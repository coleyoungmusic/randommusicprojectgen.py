from appJar import gui

import random

app = gui()

Keys = ['A', 'A#', 'B', 'C', 'C#', 'D',
       'D#', 'E', 'F', 'F#', 'G', 'G#']

Time_Signature = ['4/4', '3/4', '2/4', '6/8']

BPM = list(range(50,201))

app.setFont(25)
app.addLabelSpinBox("Key:", Keys)

app.setFont(25)
app.addLabelSpinBox("Time Signature:", Time_Signature)

app.setFont(25)
app.addLabelSpinBox("BPM:", list(range(50,201)))


def press(btn):
    random_key = random.choice(Keys)
    random_key2 = random.choice(Time_Signature)
    random_key3 = random.choice(BPM)
    app.setSpinBox("Key:", random_key, callFunction=True)
    app.setSpinBox("Time Signature:", random_key2, callFunction=True)
    app.setSpinBox("BPM:", random_key3, callFunction=True)


app.addButton("Randomize", press)

#Button will randomize the Key, BPM and Time Signature.

app.go()
