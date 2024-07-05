from tkinter import Tk, Text

root = Tk()
root.resizable(False, False)
root.title("Text Widget Example")

text = Text(root, height=8)
text.pack()

text.insert('1.0', 'Escreva algo a baixo:')

root.mainloop()
