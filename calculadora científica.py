from tkinter import *

#criando classe da calculadora

class Calculator:
# init é um método especial chamado sempre que um modelo é criado a partir da classe em python o parametro master é passado pelo usuário ao instanciar a classe 

    def __init__(self, master):
        self.master = master
        master.title("Calculadora Científica")
# Tipo de texto grade e cofiguração da tela
        self.screen = Text(master, state='disabled', width=40, height=3, background='light grey', foreground='black')
        self.screen.grid(row=0,column=0,columnspan=4,padx=5,pady=5)
        self.screen.configure(state='normal')
# Definindo todos os conteúdos dos butões
        button_text = ['7', '8', '9', '/', '4', '5', '6', '*', '1', '2', '3', '-', '0', '.', 'C', '+']
# Aqui tem-se o laço 'for' usando 'b' do originário'i' para passar por todas as strings que estão separadas por virgula
        r = 1
        c = 0
        for b in button_text:
            if b == 'C':
                Button(master, text=b, width=5, height=2, command=lambda text=b:self.clear_screen()).grid(row=r,column=c,padx=5,pady=5)
            elif b == '.':
                Button(master, text=b, width=5, height=2, command=lambda text=b:self.add_to_screen(text)).grid(row=r,column=c,padx=5,pady=5)
            elif b == '+':
                Button(master, text=b, width=5, height=2, command=lambda text=b:self.add_to_screen(text)).grid(row=r,column=c,padx=5,pady=5)
            else:
                Button(master, text=b, width=5, height=2, command=lambda text=b:self.add_to_screen(text)).grid(row=r,column=c,padx=5,pady=5)
            c += 1
            if c > 3:
                c = 0
                r += 1
        Button(master, text='=', width=5, height=2, command=lambda:self.calculate()).grid(row=r,column=0,columnspan=4,padx=5,pady=5)
# Definindo função de limpar tela ultilizando comando delete
    def clear_screen(self):
        self.screen.configure(state='normal')
        self.screen.delete('1.0', END)
# Função para o input do usuário no qual o valor do objeto também será modificavel e será inserido no fim da tela
    def add_to_screen(self, value):
        self.screen.configure(state='normal')
        self.screen.insert(END, value)

    def calculate(self):
        self.screen.configure(state='normal')
        try:
            result = eval(self.screen.get('1.0', END))
            self.screen.delete('1.0', END)
            self.screen.insert(END, result)
        except:
            self.screen.delete('1.0', END)
            self.screen.insert(END, 'Erro')

root = Tk()
calculator = Calculator(root)
root.mainloop()
