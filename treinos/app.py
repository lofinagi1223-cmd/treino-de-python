idade = int(input("qual sua idade? "));

if idade < 18 and idade >= 13:
   print("Você é adolescente")

elif idade >= 18 and idade < 60:
   print("Você é adulto")

elif idade >= 60:
   print("Você é idoso")

elif idade < 13:
   print("Você é criança")

else:
   print("Houve algum erro")