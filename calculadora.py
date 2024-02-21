#Importar as bibliotecas necessárias
from tkinter import *
from tkinter import ttk
from cores import *


#Criar a janela com configurações básicas
janela = Tk()
janela.title('Calculadora')
janela.geometry("235x310")
janela.config(bg=cor1)

#Dividir a janela em 2 partes e aplicar configurações
frameTela = Frame(janela, width=235, height=50, bg=cor3)
frameTela.grid(row=0, column=0)

frameCorpo = Frame(janela, width=235, height=260)
frameCorpo.grid(row=1, column=0)

todosValores = ''

#Criar label
valorTexto = StringVar()

#Criando função para entrada de valores
def entrarValor(valor):
    global todosValores
    todosValores += str(valor)
    #Passando valor para a tela
    valorTexto.set(todosValores)


#Função para calcular
#Função "eval()" permite executar uma string como código Python, ou seja, será interpretada como um comando Python válido
def calcular():
    global todosValores
    resultado = eval(todosValores)
    valorTexto.set(str(resultado))


#Função para limpar os valores
def limparTela():
    global todosValores
    todosValores = ''
    valorTexto.set('')


appLabel = Label(frameTela, textvariable=valorTexto, width=16, height=2, padx=7, relief=FLAT, anchor='e', justify=RIGHT, font=("Ivy 18"),bg=cor3, fg=cor2)
appLabel.place(x=0, y=0)

#Criar e configurar botões
b1 = Button(frameCorpo, command = limparTela, text="AC", width=11, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b1.place(x=0, y=0)
b2 = Button(frameCorpo, command = lambda: entrarValor('%'), text="%", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b2.place(x=118, y=0)
b3 = Button(frameCorpo, command = lambda: entrarValor('/'), text="/", width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b3.place(x=177, y=0)


b4 = Button(frameCorpo, command = lambda: entrarValor('7'), text="7", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b4.place(x=0, y=52)
b5 = Button(frameCorpo, command = lambda: entrarValor('8'), text="8", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b5.place(x=59, y=52)
b6 = Button(frameCorpo, command = lambda: entrarValor('9'), text="9", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b6.place(x=118, y=52)
b7 = Button(frameCorpo, command = lambda: entrarValor('*'), text="*", width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b7.place(x=177, y=52)


b8 = Button(frameCorpo, command = lambda: entrarValor('4'), text="4", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b8.place(x=0, y=104)
b9 = Button(frameCorpo, command = lambda: entrarValor('5'), text="5", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b9.place(x=59, y=104)
b10 = Button(frameCorpo, command = lambda: entrarValor('6'), text="6", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b10.place(x=118, y=104)
b11 = Button(frameCorpo, command = lambda: entrarValor('-'), text="-", width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b11.place(x=177, y=104)


b12 = Button(frameCorpo, command = lambda: entrarValor('1'), text="1", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b12.place(x=0, y=156)
b13 = Button(frameCorpo, command = lambda: entrarValor('2'), text="2", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b13.place(x=59, y=156)
b14 = Button(frameCorpo, command = lambda: entrarValor('3'), text="3", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b14.place(x=118, y=156)
b15 = Button(frameCorpo, command = lambda: entrarValor('+'), text="+", width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b15.place(x=177, y=156)


b16 = Button(frameCorpo, command = lambda: entrarValor('0'), text="0", width=11, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b16.place(x=0, y=208)
b17 = Button(frameCorpo, command = lambda: entrarValor('.'), text=".", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b17.place(x=118, y=208)
b18 = Button(frameCorpo, command = calcular, text="=", width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b18.place(x=177, y=208)

#Visualizar janela
janela.mainloop()