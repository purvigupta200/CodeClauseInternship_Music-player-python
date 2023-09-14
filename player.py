import tkinter as tk
import vlc

# create VLC instance
player = vlc.Instance('--no-xlib')

# create VLC media player
media = player.media_new_path("path/to/your/audio.mp3")
player = vlc.MediaPlayer()
player.set_media(media)

# create window
root = tk.Tk()
root.geometry("200x200")

# create play button
def play_button_clicked():
    player.play()

play_button = tk.Button(root, text="Play", command=play_button_clicked)
play_button.pack()

# start GUI loop
root.mainloop()