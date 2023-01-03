def listaTipoFicheiroTXT(tipoTXT):
    from os import listdir
     
    txt = 'Lista de Ficheiros : ' + tipoTXT.upper()
    print(txt)
    print('-' * len(txt)) 
    
    for fileId in listdir():
        if fileId.endswith(tipoTXT):
            print(fileId)
    
def listaTipoFicheiroCSV(tipoCSV):  
    from os import listdir
    csv = 'Lista de Ficheiros : ' + tipoCSV.upper()
    print(csv)
    print('-' * len(csv))
    
    for fileId in listdir():
        if fileId.endswith(tipoCSV):
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

def LerFicheiroTXT():
    from os.path import isfile
    dados = dict()

    listaTipoFicheiroTXT('.txt')
    nomeFile = ""
    while not isfile(nomeFile):
        nomeFile = input('Nome do Ficheiro: ')
    
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
# O problema de ter chamado global dados, foi que sempre que executo a função pede o nome do ficheiro TXT e não pode ser, mesmo no programa principal pede
#antes sequer de selecionar as opcoes do menu1. Não sei como alterar
global dados
dados = LerFicheiroTXT()

def GeradorResp():
    import random
    listResp = []
    for v in dados.values():
        Possibilidades = [random.choice(v[3]), random.choice(v[3]), random.choice(v[3]), random.choice(v[3]), random.choice(v[3]), '0']
        resposta = random.choice(Possibilidades)
        listResp.append(resposta)
    return listResp

def Perguntas():
    Perguntas = []
    for k in dados.keys():
        Perguntas.append(k)
    return Perguntas

def FicheiroRES_CSV():
    import csv
    from os.path import isfile
    listaTipoFicheiroTXT('.txt')
    fileNameTXT = input('Indique o Nome do Ficheiro TXT: ')
    while not isfile(fileNameTXT):
        print('Erro : Ficheiro não existente ou falta de .txt')
        fileNameTXT = input('Indique o Nome do Ficheiro TXT: ')
    listaTipoFicheiroCSV('.csv')
    fileNameCSV = input('Indique o Nome do Ficheiro CSV: ')
    while not isfile(fileNameCSV):
        print('Erro : Ficheiro não existente ou falta de .csv')
        fileNameCSV = input('Indique o Nome do Ficheiro CSV')
    f = open(fileNameCSV,'r')
    csv_reader = csv.reader(f)
    fileNameCSV_RES = input('Que nome deseja colocar no Ficheiro _RES.csv ? :')
    if not fileNameCSV_RES.endswith("_RES.csv"):
        print('Erro : Ficheiro não existente ou falta de _RES.csv')
        fileNameCSV_RES = input('Que nome deseja colocar no Ficheiro _RES.csv ? :')
        
    with open(fileNameCSV_RES,'w') as output:
        writer = csv.writer(output)
        Perguntas1 = Perguntas()
        Colunas = ['Alunos']
        Colunas.extend(Perguntas1)
        writer.writerow(Colunas)
        for linha in csv_reader:
            listlinha = []
            listResp = []
            listlinha.append(linha)
            listResp = GeradorResp()
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
    
