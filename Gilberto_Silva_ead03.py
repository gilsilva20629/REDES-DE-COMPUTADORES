
# Escrito por gilsilva20629@gmail.com _ gilberto.s@escolar.ifrn.edu.br

'''
	3) Implemente um programa que leia uma palavra e verifique se a mesma é palíndromo.
	Um palíndromo é uma palavra que pode ser lida igualmente de trás pra frente e de frente pra trás. Exemplo: arara.
'''


p = input('Digite uma palavra: ')
t0 = -1
r = 1


for i in p:
	if i == p[t0] :	
		t0 = t0 - 1
	else:
		r = 0

if r == 0 :
	print('false')
else:
	print('true')









'''
if :
	
	elif

else:

'''