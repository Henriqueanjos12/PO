#coding: utf-8
import random
import timeit
import matplotlib.pyplot as plt

'''
Função Selection Sort.
'''
def selection(lista):
	tamanho_lista=len(lista)
	for i in range(0,tamanho_lista-1):
		for j in range(i+1,tamanho_lista):
			if(lista[j]<lista[i]):
				aux=lista[i]
				lista[i]=lista[j]
				lista[j]=aux
			

'''
Função para gerar lista ordenada crescente.
'''
def geraLC(tamanho_lista):
	lista=[]
	for i in range(0,tamanho_lista,1):
		lista.append(i)
	return lista

'''
Função para gerar lista aleatória com repetição.
'''
def geraLACR(tamanho_lista):
	lista=[]
	for i in  range(0,tamanho_lista,1):
		lista.append(random.randint(0,tamanho_lista-1))
	return lista

'''
Função para gerar lista aleatória sem repetição.
'''
def geraLASR(tamanho_lista):
	lista=geraLC(tamanho_lista)
	random.shuffle(lista)
	return lista

'''
Função para gerar lista ordenada decrescente.
'''
def geraLD(tamanho_lista):
	lista=[]
	for i in range(tamanho_lista-1,-1,-1):
		lista.append(i)
	return lista

"""
Listas.
"""
lc=[geraLC(1000),geraLC(10000),geraLC(30000),geraLC(60000)]
lacr=[geraLACR(1000),geraLACR(10000),geraLACR(30000),geraLACR(60000)]
lasr=[geraLASR(1000),geraLASR(10000),geraLASR(30000),geraLASR(60000)]
ld=[geraLD(1000),geraLD(10000),geraLD(30000),geraLD(60000)]
tam=[1000,10000,30000,60000]



'''
Listas x e y para plotar gráfico.
'''
#Lista ordenada crescente
xlc=[]
ylc=[]

#Lista aleatória com repetição
xlacr=[]
ylacr=[]

#Lista aleatória sem repetição
xlasr=[]
ylasr=[]

#Lista ordenada decrescente
xld=[]
yld=[]

'''
Medindo o tempo.
'''
for i in range(4):
	#Lista ordenada crescente
	xlc.append(timeit.timeit("selection({})".format(lc[i]), setup="from __main__ import selection",number=1))
	ylc.append(tam[i])
	print (xlc[i],",",ylc[i])

	#Lista aleatória com repetição
	xlacr.append(timeit.timeit("selection({})".format(lacr[i]), setup="from __main__ import selection",number=1))
	ylacr.append(tam[i])
	print (xlacr[i],",",ylacr[i])
	
	#Lista aleatória sem repetição
	xlasr.append(timeit.timeit("selection({})".format(lasr[i]), setup="from __main__ import selection",number=1))
	ylasr.append(tam[i])
	print (xlasr[i],",",ylasr[i])
	
	#Lista ordenada decrescente
	xld.append(timeit.timeit("selection({})".format(ld[i]), setup="from __main__ import selection",number=1))
	yld.append(tam[i])
	print (xld[i],",",yld[i])
	
	
"""
Plotando o gráfico.
"""
#Lista ordenada crescente
plt.plot(xlc, ylc, Color='green', label='Lista Crescente')

#Lista aleatória com repetição
plt.plot(xlacr, ylacr, Color='yellow', label='Lista Aleatória Com Repetição')

#Lista aleatória sem repetição
plt.plot(xlasr, ylasr, Color='blue', label='Lista Aleatória Sem Repetição')

#Lista ordenada decrescente
plt.plot(xld, yld, Color='red', label='Lista Decrescente')

'''
Configurações do gráfico - legenda, título e eixos x e y.
'''
plt.legend(loc=0)
plt.title('Selection Sort - Luiz Henrique')
plt.xlabel('Tempo(s)')
plt.ylabel('Tamanho da Lista')

'''
Mostrando o gráfico.
'''
plt.show()
