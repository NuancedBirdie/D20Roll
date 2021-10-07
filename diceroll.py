import tkinter as tk
import random
from gtts import gTTS
import os
import playsound

def diceroll():
    lbl_value["text"] = f"{random.randint(1,20)}"

    tts = gTTS(text =lbl_value["text"], lang='eo')
    filename="DaniTemp.mp3"
    tts.save(filename)    
    playsound.playsound(filename)
    os.remove(filename)

window = tk.Tk()
window.geometry("75x75")

btn_roll = tk.Button(master=window, relief=tk.RAISED, text="Roll", command=diceroll)
btn_roll.pack(side=tk.TOP)

lbl_value = tk.Label(master=window, text="-")
lbl_value.pack(side=tk.BOTTOM)


window.resizable(False,False)

window.mainloop()