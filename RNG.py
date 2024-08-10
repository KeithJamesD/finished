import random
from tkinter import Tk, Label, Button

class RandomNumberGenerator:
    def __init__(self, master):
        self.master = master
        master.title("RNG")

        self.label = Label(master, text="Click")
        self.label.pack()

        self.generate_button = Button(master, text="GO", command=self.generate_random_number)
        self.generate_button.pack()

        self.result_label = Label(master, text="")
        self.result_label.pack()

    def generate_random_number(self):
        random_number = random.randint(1, 100)
        self.result_label.config(text=f"{random_number}")

root = Tk()
my_gui = RandomNumberGenerator(root)
root.mainloop()
