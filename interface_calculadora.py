import tkinter as tk

from calculadora_v1 import calcular

janela = tk.Tk()
janela.title("Teste")

campo_num1 = tk.Entry(janela)
campo_num1.pack()
campo_num2 = tk.Entry(janela)
campo_num2.pack()

resultado_label = tk.Label(janela, text="")
resultado_label.pack()
   
def clique_soma():
    numero1 = float(campo_num1.get())
    numero2 = float(campo_num2.get())
    resultado = calcular(numero1, numero2, "1")
    resultado_label.config(text=resultado)

def clique_subtracao():
    numero1 = float(campo_num1.get())
    numero2 = float(campo_num2.get())
    resultado = calcular(numero1, numero2, "2")
    resultado_label.config(text=resultado)

def clique_multiplicacao():
    numero1 = float(campo_num1.get())
    numero2 = float(campo_num2.get())
    resultado = calcular(numero1, numero2, "3")
    resultado_label.config(text=resultado)

def clique_divisao():
    numero1 = float(campo_num1.get())
    numero2 = float(campo_num2.get())
    resultado = calcular(numero1, numero2, "4")
    resultado_label.config(text=resultado)

botao_soma = tk.Button(janela, text="Somar", command=clique_soma)
botao_soma.pack()

botao_subtracao = tk.Button(janela, text="Subtrair", command=clique_subtracao)
botao_subtracao.pack() 

botao_multiplicacao = tk.Button(janela, text="Multiplicar", command=clique_multiplicacao)
botao_multiplicacao.pack()

botao_divisao = tk.Button(janela, text="Dividir", command=clique_divisao)
botao_divisao.pack()

janela.mainloop()