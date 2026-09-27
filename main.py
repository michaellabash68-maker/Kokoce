import tkinter as tk
import webbrowser
VIDEO_URL = "https://youtu.be/_PlEyLKnmaE"
window = tk.Tk()
window.title("Video Player")
window.geometry("400x200")
def play_video():
    webbrowser.open(VIDEO_URL)
def exit_program():
    window.destroy()
tk.Label(
    window,
    text="Click the button to play the video.",
    font=("Arial", 12)
).pack(pady=30)
tk.Button(
    window,
    text="Play Video",
    command=play_video,
    width=20
).pack(pady=5)
tk.Button(
    window,
    text="Exit",
    command=exit_program,
    width=20
).pack(pady=5)
window.mainloop()