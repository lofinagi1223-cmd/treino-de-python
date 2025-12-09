#elabore uma função que descreva se a palavra é um palíndromo ou não

def achar_palindromo(palavra):

   palavra = palavra.lower()

   invertida = ""

   for i in range (len(palavra) -1, -1, -1):
      invertida = invertida + palavra[i]

   if palavra == invertida:
    return True
   else:
     return False


print (achar_palindromo(""))