import tkinter as tk

janela = tk.Tk()
janela.resizable(False, False)
janela.title("Text Widget Example")

text = tk.Text(janela, height=10)
text.pack()



label = tk.Label(janela)
label.pack()

botao_tentar_novamente = tk.Button(janela)
botao_tentar_novamente.pack()
botao_sair = tk.Button(janela)
botao_sair.pack()

def verificar_tamanho(event):
    tamanho = text.get('1.0', '2.0')
    if len (tamanho) > 2:
        text['state'] = 'disable'
       
        #label.config(text="Exedeu Limite", bg='purple', fg='silver', font = 'Arial 10')
      
      
    else:
        text['state'] = 'normal'



def zerar_texto(event): 
    botao_tentar_novamente.config(janela, text="Clique para tentar novamente",bg='blue', fg='white')
    botao_sair.config(janela, text="Clique para sair",bg='red', fg='white')


janela.bind('<KeyRelease>', verificar_tamanho)

 

janela.mainloop()