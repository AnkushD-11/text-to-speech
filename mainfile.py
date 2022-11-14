from gtts import gTTS
import os
from tkinter import *
import tkinter as tk

enter_text = ""

language = 'en'

voice = gTTS(text= enter_text, lang= language, slow= False)
voice.save("File.mp3")
os.system("start file.mp3")
