#tela1.py



import tkinter as tk


#cria uma instância de uma janela
janela = tk.Tk()


janela.title('Bem vindo ao Tkinter')

label = tk.Label(janela, text='Este é um label', font=('Arial Bold', 70))
label.grid(column=0, row=0)


janela.mainloop()
