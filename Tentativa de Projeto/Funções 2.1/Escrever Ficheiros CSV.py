# -*- coding: utf-8 -*-
"""
Created on Mon Jan  2 14:49:26 2023

@author: david
"""

#Construção dos números de estudante 
  
def constroiNumero(lista):
    from random import randint
    n=0
    while n!=1:
        aaaa = randint(2018,2022)
        bbbb = randint(1000,2000)
        aaaabbbb = str(aaaa) + str(bbbb)
        
        if aaaabbbb not in lista:
            lista.append(aaaabbbb)
            n=1
    return lista


#Construção dos Nomes e Apelidos dos Estudantes

def constroiNomeApelido():
    from random import randint
    
    nomes = ('Alexandre','Bruno','Ana','Carla','Tomé','João','Mafalda','José','Irene','Beatriz','Ivo','Carlota','Júlio','Kévin','Susana','Simone','Tiago','Eduardo','Telmo','Vanessa','Teresa','Vasco')
    apelidos = ('Silva','Simões','Faria','Costa','Oliveira','Fernandes','Ribeiro','Gomes','Neves','Matos','Alves')
    
    nomeApelido = ''
    nomeApelido += nomes[randint(0,len(nomes)-1)]
    nomeApelido += ' ' + apelidos[randint(0,len(apelidos)-1)]
    return nomeApelido 


#Escrever Ficheiro CSV
import csv

def escreveFicheirosCSV():
    nomeFile = input('Nome do Ficheiro CSV:')
    if not nomeFile.endswith('.csv'):
        print('Error: o ficheiro deve ter a extensão .csv')
        return
    
    try:
        N = int(input('Número de Estudantes: '))
    except ValueError:
        print('Error: o número de estudantes deve ser um inteiro positivo')
        return
    if N <= 0:
        print('Error: o número de estudantes deve ser um inteiro positivo')
        return

    with open(nomeFile, 'w', newline='') as fileId:
        csvFile = csv.DictWriter(fileId, fieldnames=['Número', 'Nome e Apelido'], delimiter=',')
        for i in range(N):
            numero = constroiNumero([])
            nome = constroiNomeApelido()
            csvFile.writerow({'Número': numero, 'Nome e Apelido': nome})


            
    
