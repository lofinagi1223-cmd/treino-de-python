def saudacao(nome):  #parametros
   print("Olá, pessoa!", nome)   
                                
saudacao("Ismael")   #argumentos
saudacao("Jó")       #argumentos


def soma(a,b):
   return a+b

resultado = soma(3,4)
print(resultado)


def area_retangulo(base, altura):
    """
    Calcula a área de um retângulo.


    Args:
        base (float): A base do retângulo.
        altura (float): A altura do retângulo.


    Returns:
        float: A área do retângulo.
    """
    return base * altura

print(area_retangulo(10,111))

#O bloco finally é opcional e é executado sempre, independentemente de ter ocorrido uma exceção ou não. É comumente utilizado para realizar tarefas de limpeza ou liberação de recursos.

#O bloco except especifica o tipo de exceção que se deseja capturar e lidar. Você pode ter múltiplos blocos except para lidar com diferentes tipos de exceções.


nome = input("Qual seu nome? ")

print(f'Oi, '+ nome)