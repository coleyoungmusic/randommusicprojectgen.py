from appJar import gui

import random

app = gui()

app.setFont(25)
app.addLabelSpinBox("Key:", ['A', 'A#', 'B', 'C', 'C#', 'D',
                            'D#', 'E', 'F', 'F#', 'G', 'G#'])

app.setFont(25)
app.addLabelSpinBox("Time Signature:", ['4/4', '3/4', '2/4', '6/8'])

app.setFont(25)
app.addLabelSpinBox("Bpm:", list(range(50,201)))


def press(btn):
    print(btn)


app.addButton("Randomize", press)

#Button will randomize the Key, BPM and Time Signature.


app.go()