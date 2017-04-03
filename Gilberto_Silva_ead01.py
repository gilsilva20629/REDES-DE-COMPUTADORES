
# Escrito por gilsilva20629@gmail.com or gilberto.s@escolar.ifrn.edu.br

'''
	1) Faça um programa que leia uma frase e determine quantas vezes
	um determinado caractere, também informado pelo usuário, ocorre na frase.
'''


frase = input('Digite uma frase: ')
c = input('Digite um caractere da frase: ')
temp = 0 

for i in frase:
	if c == i :
		temp = temp + 1

print (temp)
