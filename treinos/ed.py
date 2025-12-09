'''frutas = ["maçã", "uva", "morango"]

print(frutas[-1])
print(frutas[1])
print(frutas[0])'''

frutas = ["maçã", "uva", "morango"]

frutas.append("melancia")
print(frutas)

frutas.insert(1, "laranja")
print(frutas)

frutas.remove("morango")
print(frutas)

fruta_removida = frutas.pop(2)
print(frutas)
print(fruta_removida)

frutas.sort() #organiza
print(frutas)

frutas.reverse()
print(frutas)



#Importante, porque gostei
#nova_lista = [expressão for elemento in sequência if condição]


numeros = [10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100]
divisor = [x * 10 for x in numeros if x > 5]
print(divisor)