from tkinter import *
from cell import Cell
import settings
import utils
# this is from a tutorial - to learn about OOP and Gui 
# https://www.youtube.com/watch?v=OqbGRZx4xUc

root = Tk()
# creates a window
root.configure(bg="black")
root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')
# sets window size
root.title("Minesweeper Game")
# changes app title
root.resizable(False, False)
# disallows resizing

top_frame = Frame(
    root,
    bg="black", # change later to black
    width=utils.width_prct(100),
    height=utils.height_prct(25)
)
top_frame.place(x=0, y=0)

left_frame = Frame(
    root,
    bg="black", # change later to black
    width=utils.width_prct(25),
    height=utils.height_prct(75)
)
left_frame.place(x=0, y=utils.height_prct(25))

center_frame = Frame(
    root,
    bg='black', #change to black
    width=utils.width_prct(75),
    height=utils.height_prct(75),

)
center_frame.place(
    x=utils.width_prct(25),
    y=utils.height_prct(25)
)

c1 = Cell()
c1.create_btn_object(center_frame)
c1.cell_btn_object.place(
    x=0,
    y=0
)



# makes it keep running until closed
root.mainloop()
