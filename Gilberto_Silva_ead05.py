# Escrito por gilsilva20629@gmail.com or gilberto.s@escolar.ifrn.edu.br

'''
	Faça um programa que leia um nome completo e apresente-o da seguinte forma:
Nome: João Maria Silva Resultado: Silva, João
'''

nome = input()
#print(type(nome))
#print ('\n')
nome = nome.split()
#print(type(nome))
#print ('\n')
#print (len(nome))
tam = len(nome)
#print ('\n')
print(nome[tam-1]+ ', ' + (nome[0]) )