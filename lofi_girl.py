import tkinter as tk
import pygame

def play_song():
    pygame.mixer.init()
    pygame.mixer.music.load("music.mp3")
    pygame.mixer.music.play()

def pause_song():
    pygame.mixer.music.pause()

def unpause_song():
    pygame.mixer.music.unpause()

forward_count = 0

def skip_forward():
    global forward_count
    current_time = pygame.mixer.music.get_pos() / 1000
    new_time = current_time + (forward_count * 10)
    pygame.mixer.music.set_pos(new_time)
    forward_count += 1

window = tk.Tk()
window.title("Lofi Girl")

canvas = tk.Canvas(window, width=500, height=500)
canvas.pack()

background_image = tk.PhotoImage(file="lofi_girl.png")
canvas.create_image(0, 0, anchor=tk.NW, image=background_image)

play_button = tk.Button(canvas, text="Start", command=play_song, bg="cyan", fg="black", font=("Arial", 12, "bold"), highlightthickness=-1, highlightbackground="white")
play_button.place(x=10, y=10)

pause_button = tk.Button(canvas, text="Pause", command=pause_song, bg="cyan", fg="black", font=("Arial", 12, "bold"), highlightthickness=-1, highlightbackground="white")
pause_button.place(relx=0.5, rely=0.9, anchor=tk.CENTER, x=-80, y=-40)

unpause_button = tk.Button(canvas, text="Plat", command=unpause_song, bg="cyan", fg="black", font=("Arial", 12, "bold"), highlightthickness=-1, highlightbackground="white")
unpause_button.place(relx=0.5, rely=0.9, anchor=tk.CENTER, y=-40)

skip_button = tk.Button(canvas, text="Forward", command=skip_forward, bg="cyan", fg="black", font=("Arial", 12, "bold"), highlightthickness=-1, highlightbackground="white")
skip_button.place(relx=0.5, rely=0.9, anchor=tk.CENTER, x=80, y=-40)

window.mainloop()
