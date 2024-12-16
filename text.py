
import pygame
from gtts import gTTS
from tkinter import *
import os


def play_sound():
    text = entry.get()  
    if text: 

        save_path = os.path.join(os.getcwd(), "test.mp3")
        
        try:

            tts = gTTS(text=text, lang='en')
            
            tts.save(save_path)
            
            if os.path.exists(save_path):
                print(f"File saved successfully at {save_path}")
            else:
                print("Error: File not saved.")
                return

            pygame.mixer.init()

            pygame.mixer.music.load(save_path)
            pygame.mixer.music.play()
            print("Playing sound...")
            
            entry.delete(0, END)
            
        except PermissionError:
            print("Permission denied to save the audio file. Try running as administrator or choosing another path.")
        except Exception as e:
            print(f"Error: {e}")
    else:
        print("No text entered.")  

scr = Tk()
scr.geometry("350x300")
scr.resizable(0, 0)

entry = Entry(scr, width=30)
entry.pack(pady=10)

button = Button(scr, text="Play Sound", command=play_sound)
button.pack(pady=20)

scr.mainloop()




