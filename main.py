from tkinter import *


root = Tk()
# creates a window
root.configure(bg="black")
root.geometry("1440x720")
# sets window size
root.title("Minesweeper Game")
# changes app title
root.resizable(False, False)
# disallows resizing

top_frame = Frame(
    root,
    bg="red", # change later to black
    width=1440,
    height=180
)
top_frame.place(x=0, y=0)

left_frame = Frame(
    root,
    bg="blue", # change later to black
    width=360,
    height=540
)


root.mainloop()
# makes it keep running until closed
