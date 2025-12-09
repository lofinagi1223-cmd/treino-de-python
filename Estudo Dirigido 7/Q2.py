#crie uma função que leia um numero de telefone e corrija o numero no caso deste conter apenas 7 digitos acrescentando
# um 3 na frente. O usuario pode informar o numero com ou sem traço

def corrigir_telefone(numero):

    numero = numero.replace("-", "")

    if len(numero) == 7:
        numero = "3" + numero
    return numero


   # ---- Exemplo de uso ----

telefone = input("Digite o número de telefone: ")

telefone_arrumado = corrigir_telefone(telefone)

print("Número corrigido:", telefone_arrumado)