import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.resizable(False, False)
root.title("Scrollbar Widget Example")

# apply the grid layout
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)

# create the text widget
text = tk.Text(root, height=10)
text.grid(row=0, column=20, sticky=tk.EW) #Foi modificado o nº da coluna

# create a scrollbar widget and set its command to the text widget
scrollbar = ttk.Scrollbar(root, orient='vertical', command=text.yview)#yview faz com que a scroll bar mexa de forma vertical no texto
scrollbar.grid(row=0, column=1, sticky=tk.NS)

#  communicate back to the scrollbar , sem isso a scrool bar não se mexe
text['yscrollcommand'] = scrollbar.set

# add sample text to the text widget to show the screen
for i in range(1,50):
    position = f'{i}.0'
    text.insert(position,f'Line {i}\n');

root.mainloop()