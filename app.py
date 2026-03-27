import tkinter as tk
import imageio
from PIL import Image, ImageTk
import sys, os

def resource_path(file):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, file)
    return os.path.join(os.path.abspath("."), file)

VIDEO = resource_path("video.mp4")

root = tk.Tk()
root.attributes("-fullscreen", True)
root.configure(bg="black")

canvas = tk.Canvas(root, highlightthickness=0)
canvas.pack(fill="both", expand=True)

text = canvas.create_text(
    500, 100,
    text="INITIALIZING...",
    fill="lime",
    font=("Consolas", 30)
)

reader = imageio.get_reader(VIDEO)

def update_frame():
    try:
        frame = next(reader)
        img = Image.fromarray(frame)
        img = img.resize((root.winfo_screenwidth(), root.winfo_screenheight()))
        imgtk = ImageTk.PhotoImage(img)

        canvas.create_image(0, 0, anchor="nw", image=imgtk)
        canvas.image = imgtk

        root.after(30, update_frame)
    except:
        reader.close()

update_frame()

def exit_app(e=None):
    root.destroy()

root.bind("<Escape>", exit_app)

root.mainloop()
