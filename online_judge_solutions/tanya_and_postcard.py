#tanya and postcard

mensagem = [j for j in raw_input()]
jornal = [j for j in raw_input()]

letras = {}

for i in jornal:
	if i not in letras:
		letras[i] = 1
	else:
		letras[i] += 1

yay = 0
whoops = 0

for i in range(0, len(mensagem)):
	if letras.get(mensagem[i]) != None and letras.get(mensagem[i]) > 0:
		letras[mensagem[i]] -= 1
		yay += 1
		mensagem[i] = "*"
		
for letra in mensagem:
	if letras.get(letra.lower()) != None and letras.get(letra.lower()) > 0:
		letras[letra.lower()] -= 1
		whoops += 1
	
	elif letras.get(letra.upper()) != None and letras.get(letra.upper()) > 0:
		letras[letra.upper()] -= 1
		whoops += 1

print yay, whoops
