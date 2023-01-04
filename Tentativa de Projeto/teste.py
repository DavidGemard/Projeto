# -*- coding: utf-8 -*-
"""
Created on Wed Jan  4 08:56:00 2023

@author: david
"""            
def listaTipoFicheiro(tipo):
    from os import listdir
    
    txt = 'Lista de Ficheiros ' + tipo.upper()
    print(txt)
    print('-' * len(txt))
    
    
    for fileId in listdir():
        if fileId.endswith(tipo):
            print(fileId)
            
#CRIAÇÃO DE MENUS
def Menu1():
    k=30
    print ('Menu Principal'.center(k)) #Centrar a cadeia de caracteres no meio de 30
    print ('-' * k) # vai colocar o número de traços correspondente ao número de k
    print ('1 - Construir Respostas')
    print ('2 - Analisar Resultados')
    print ('0 - SAIR')
    print ('-' * k)
    
#Funções de Controlo do Menu1

def LerTesteTXT(nomeFile):
    dados = dict()    
    Perg = '--> Pergunta: <--'
    ResA = 'Resposta: ...... A'
    ResB = 'Resposta: ...... B'
    ResC = 'Resposta: ...... C'
    ResD = 'Resposta: ...... D'
    Resp_Possiveis = [ResA, ResB, ResC, ResD]

    with open(nomeFile, 'r') as fileId:
        for linha in fileId:
            linha = linha.strip()

            if linha != ResA and linha != ResB and linha != ResC and linha != ResD and linha != Perg:
                NPerg = linha
                TxtPerg = fileId.readline().strip()
                OpCerta = fileId.readline().strip()
                Opcoes = []
                linha = fileId.readline().strip()
                while linha in Resp_Possiveis:
                    Opcoes.append(linha)
                    linha = fileId.readline().strip()
                dados[NPerg] = [NPerg, TxtPerg, OpCerta, Opcoes]
    
    return dados

def leFicheiroCSV(nomeFile):
    from csv import reader
    dados = list()
    fileId = open(nomeFile,'r')
    csvFile = reader(fileId,delimiter = ',')
    for i in csvFile:
        dados.append(i)
    fileId.close()
    return dados

def LeFicheiros():
    from os.path import isfile
    nome = ''
    listaTipoFicheiro('.txt')
    nomeFile = input('Indique o nome do Ficheiro TXT : ')
    while not isfile(nomeFile):
        print('ERRO : Nome de Ficheiro Incorreto ou falta de .txt')
        nomeFile = input('Indique o nome do Ficheiro TXT : ')
    testeTXT = LerTesteTXT(nomeFile)
    nome = nomeFile[-4]
    
    listaTipoFicheiro('.csv')
    nomeFile = input('Indique o nome do Ficheiro CSV : ')
    while not isfile(nomeFile):
        print('ERRO : Nome de Ficheiro Incorreto ou falta de .csv')
        nomeFile = input('Indique o nome do Ficheiro CSV : ')
        
    alunos = leFicheiroCSV(nomeFile)
    nome += '-' + nomeFile[-4]
    
    return nome, testeTXT, alunos
    
def GeradorResp(nomeFile):
    import random
    dados = LerTesteTXT(nomeFile)
    listResp = []
    for v in dados.values():
        Possibilidades = [random.choice(v[3]),'0']
        Resp = random.choice(Possibilidades)
        listResp.append(Resp)
    return listResp

def Perguntas(nomeFile):
    dados = LerTesteTXT(nomeFile)
    Perguntas = []
    for k in dados.keys():
        Perguntas.append(k)
    return Perguntas

def FicheiroRES_CSV():
    import csv
    from os.path import isfile
    listaTipoFicheiro('.txt')
    nomeFile = input('Indique o Nome do Ficheiro TXT: ')
    while not isfile(nomeFile):
        print('Erro : Ficheiro não existente ou falta de .txt')
        nomeFile = input('Indique o Nome do Ficheiro TXT: ')
    listaTipoFicheiro('.csv')
    nomeFile = input('Indique o Nome do Ficheiro CSV: ')
    while not isfile(nomeFile):
        print('Erro : Ficheiro não existente ou falta de .csv')
        nomeFile = input('Indique o Nome do Ficheiro CSV: ')
    f = open(nomeFile,'r')
    csv_reader = csv.reader(f)
    listaTipoFicheiro('_RES.csv')
    nomeFileCSV_RES = input('Que nome deseja colocar no Ficheiro _RES.csv ? :')
    if not nomeFileCSV_RES.endswith("_RES.csv"):
        print('Erro : Ficheiro não existente ou falta de _RES.csv')
        nomeFileCSV_RES= input('Que nome deseja colocar no Ficheiro _RES.csv ? :')
        
    with open(nomeFileCSV_RES,'w') as output:
        writer = csv.writer(output)
        Perguntas1 = Perguntas(nomeFile)
        Colunas = ['Alunos']
        Colunas.extend(Perguntas1)
        writer.writerow(Colunas)
        for linha in csv_reader:
            listlinha = []
            listResp = []
            listlinha.append(linha)
            listResp = GeradorResp(nomeFile)
            listlinha.extend(listResp)
            writer.writerow(listlinha)
        else:
            f.close()
       
        
        
    
    
        
#Construção dos Números dos Alunos  
  
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
    
#Construção dos Nomes e Apelidos dos Alunos 

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




       
    
#Opção de Sair
def perguntaSair():
    sair = False
    op = input(' Deseja mesmo Sair (sim)? ')
    if op.lower() == 'sim':
        sair = True
    return sair 
    