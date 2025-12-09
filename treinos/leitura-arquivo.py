arquivo = open("dados.txt", "r")
conteudo = arquivo.read()
print(conteudo)
arquivo.close

arquivo = open("dados.txt", "w")
arquivo.write("Lol")
arquivo.close


x = 5
y = "3"
z = x + int(y)
print(z)