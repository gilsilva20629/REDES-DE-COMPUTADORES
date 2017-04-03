
# Escrito por gilsilva20629@gmail.com _ gilberto.s@escolar.ifrn.edu.br

'''
	4) "Faca um programa que leia uma frase e depois altere a sequencia de suas palavras pondo as em ordem alfabetica"
'''

'''
def left_shift_str(strX, idx0, idx1):
	t0 = strX[idx0]
	i0 = idx0
	i1 = (idx0 + 1)
	for i in range( idx0 , idx1 ):
		strX[i0] = strX[i1]
		i0 = i0 + 1
		i1 = i1 +1
	strX[i1] = t0
	return strX

a = 'uoiea'
print (left_shift_str(a, 0,4))
'''


str1 = input('Digite uma frase: ') 
#print(type(str1))
#print ('\n')
str1 = str1.split()
#print(type(str1))
#print ('\n')
#print (str1)
#print ('\n')	
str1 = sorted(str1)
print(str1)




