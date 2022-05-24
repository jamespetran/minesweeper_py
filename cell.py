from tkinter import Button, Label
import random
import settings


class Cell:
    all = []
    cell_count_label_object = None
    def __init__(self, x, y, is_mine=False):
        self.is_mine = is_mine
        self.cell_btn_object = None
        self.x = x
        self.y = y

        # append the object to the cell.all list
        Cell.all.append(self)

    def create_btn_object(self, location):
        btn = Button(
            location,
            width=12,
            height=4,
            # text=f"{self.x},{self.y}"
        )
        btn.bind('<Button-1>', self.left_click_actions)
        btn.bind('<Button-3>', self.right_click_actions)
        self.cell_btn_object = btn

    # this is not an instanced method; we only call it once during each game
    # therefore: this should be a static method
    # this method is only used for the class as a whole and not for each instance
    # don't need to call self in the arguments if it is not an instanced method
    @staticmethod
    def create_cell_count_label(location):
        lbl = Label(
            location,
            bg='black',
            fg='white',
            text=f"Cells Left: {settings.CELL_COUNT}",
            font=("arial", 30)
        )
        Cell.cell_count_label_object = lbl
        
    def left_click_actions(self, event):
        if self.is_mine:
            self.show_mine()
        else:
            if self.surrounded_cells_mines_length == 0:
                for cell_obj in self.surrounded_cells:
                    cell_obj.show_cell()
            self.show_cell()

    def get_cell_by_axis(self, x, y):
        # Return a cell object based on the value of x,y
        for cell in Cell.all:
            if cell.x == x and cell.y ==y:
                return cell
    
    # the @property ~DECORATOR~ denotes that this is a read only attribute 
    @property
    def surrounded_cells(self):
        cells = [
            self.get_cell_by_axis(self.x-1, self.y-1),
            self.get_cell_by_axis(self.x-1, self.y),
            self.get_cell_by_axis(self.x-1, self.y+1),
            self.get_cell_by_axis(self.x, self.y-1),
            self.get_cell_by_axis(self.x, self.y+1),            
            self.get_cell_by_axis(self.x+1, self.y-1),
            self.get_cell_by_axis(self.x+1, self.y),
            self.get_cell_by_axis(self.x+1, self.y+1),
        ]
        # this removes the None values from the cell
        cells = [cell for cell in cells if cell is not None]
        return cells

    # the @property ~DECORATOR~ denotes that this is a read only attribute 
    @property
    def surrounded_cells_mines_length(self):
        counter = 0
        for cell in self.surrounded_cells:
            if cell.is_mine:
                counter += 1
        return counter

    def show_cell(self):
        # print(self.surrounded_cells_mines_length)
        self.cell_btn_object.configure(text=self.surrounded_cells_mines_length)

    def show_mine(self):
        # a logic to interrupt the game and display a message that player lost
        self.cell_btn_object.configure(bg='red')

    def right_click_actions(self, event):
        print(event)
        print("I am right clicked!")

    # static method
    @staticmethod
    def randomize_mines():
        picked_cells = random.sample(
            Cell.all, settings.MINES_COUNT
        )
        for picked_cell in picked_cells:
            picked_cell.is_mine = True

    def __repr__(self):
        return f"Cell({self.x}, {self.y})"