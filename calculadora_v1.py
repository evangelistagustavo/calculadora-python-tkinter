def pedir_numero(mensagem):
    sucesso = False
    while sucesso == False:
        try:
            numero = float(input(mensagem))
            sucesso = True
            return numero
        except:
            print("Não deu pra converter isso em número")

def calcular(numero1, numero2, operacao):
    if operacao == "1":
        return numero1 + numero2    
    elif operacao == "2":
        return numero1 - numero2
    elif operacao == "3":
        return numero1 * numero2    
    elif operacao == "4":
        if numero2 != 0:
            return numero1 / numero2
        else:
            return "Não é possível dividir por zero"
    else:
        return "Operação inválida"

if __name__ == "__main__":
    operacao = input("Escolha um número para a operação: 1 - soma, 2 - subtração, 3 - multiplicação, 4 - divisão: ")
    numero1 = pedir_numero("Insira o primeiro número: ")
    numero2 = pedir_numero("Insira o segundo número: ")
    resultado = calcular(numero1, numero2, operacao)
    print("Resultado:", resultado)