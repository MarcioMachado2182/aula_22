import tkinter as tk

janela = tk.Tk()
janela.resizable(False, False)
janela.title("Text Widget Example")

text = tk.Text(janela, height=10)
text.pack()

label = tk.Label(janela)
label.pack()
def verificar_tamanho(event):
    tamanho = text.get('1.0', '2.0')
    if len (tamanho) > 5:
        text['state'] = 'disable'
        #print('exedeu limite')
        label.config(text="Exedeu Limite", bg='blue', fg='white', font = 'Arial 20')
      
    else:
        text['state'] = 'normal'

janela.bind('<KeyRelease>', verificar_tamanho)

 

janela.mainloop()